"""Run notebooks under a watchdog and compare their solver results with the
outputs stored in the notebooks.

The CI job runs each notebook with `pytest --nbval-lax` and the released
solvers. This script is for longer local or scheduled runs, for example to
check new builds of AMPL or of the solvers before a release:

- each notebook runs in its own process tree, in a copy of its folder (the
  repository is not modified), with a timeout per cell, a timeout per
  notebook and a memory limit; when free memory falls below a reserve, the
  largest running notebook is stopped;
- a notebook's own solver time limits (`lim:time=`, `timelim=`,
  `timelimit=`, `TimeLimit=`, `time_limit =`, `maxtime=`, with a literal
  value, outside comments) raise the cell timeout to the largest limit
  times 1.3 plus 60 seconds, and the notebook timeout to the sum of these
  over the cells that set a limit or, after one is set, solve (at least
  twice the cell timeout);
- processes that a notebook leaves running (AMPL and solvers of a stopped
  kernel) are killed;
- the solver messages (status and objective value, within --rel-tol) are
  compared cell by cell with the stored outputs; notebooks with random
  data and no seed are marked, as their objective values change from run to run, and so are
  notebooks that print "Using synthetic data" (generated instead of
  downloaded data, see --synthetic-data);
- results go to OUT/results.jsonl (one line per notebook, written as each
  finishes; a rerun skips the notebooks already there) and OUT/summary.md;
  OUT must be in notebook-runs/ or outside the repository.

With --bin-dir, the given directories (AMPL and solver executables) are put
first on PATH, and `ampl_notebook()` only creates `AMPL()` and registers the
magics: it installs no modules and activates no license (use --licfile for
an AMPL license file). It is replaced when amplpy is imported, also when the
notebook's own `%pip` installs amplpy, and the directories are put first on
PATH again then, as importing amplpy puts the module directories first.
With --skip-pip, `%pip install` lines are commented out: the packages must
already be installed. With --synthetic-data, COLAB_SYNTHETIC_DATA=1 is set:
notebooks that download data (stock prices from Yahoo Finance) generate it
instead.

Requires nbclient, nbformat, ipykernel and psutil (memory limits, cleanup of
left-over processes). TESTING.md describes the setup, how
this differs from CI, and how to read the comparison.

Examples, from the repository root:

    # the notebooks that CI runs, two at a time
    python scripts/run_notebooks.py --out notebook-runs/today

    # selected notebooks with other AMPL and solver builds
    python scripts/run_notebooks.py --list my_list.txt --out notebook-runs/build \\
        --bin-dir /path/to/ampl --bin-dir /path/to/solvers \\
        --licfile /path/to/ampl.lic --skip-pip

    # recompute the comparison and the summary of a finished run
    python scripts/run_notebooks.py --out notebook-runs/today --recompare
"""

import argparse
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

PRELUDE = """# Added by scripts/run_notebooks.py: not part of the notebook.
import os as _os
import sys as _sys
from importlib.machinery import PathFinder as _PathFinder  # not in find_spec


def _runner_env():
    if {prefix!r}:
        _os.environ["PATH"] = {prefix!r} + _os.pathsep + _os.environ["PATH"]
    if {licfile!r}:
        _os.environ["AMPL_LICFILE"] = {licfile!r}


def _runner_ampl_notebook(modules=None, license_uuid=None, **kwargs):
    from amplpy import AMPL, register_magics
    from IPython import get_ipython

    g = kwargs.get("globals_", kwargs.get("g")) or get_ipython().user_global_ns
    _runner_env()
    g["ampl"] = AMPL()
    try:  # table handlers (amplxl, ...) for an AMPL outside the modules
        import ampl_module_plugins as _pl

        _dir = _os.path.join(_os.path.dirname(_pl.__file__), "bin")
        _cur = g["ampl"].option["ampl_libpath"]  # may be empty or None
        g["ampl"].option["ampl_libpath"] = _cur + "\\n" + _dir if _cur else _dir
    except ImportError:
        pass
    print(" / ".join(g["ampl"].option["version"].split("\\n")[:2]))
    register_magics(ampl_object="ampl", globals_=g)
    return g["ampl"]


def _runner_patch(amplpy):
    amplpy.ampl_notebook = _runner_ampl_notebook
    try:
        import amplpy.vendor.ampltools as _vt

        _vt.ampl_notebook = _runner_ampl_notebook
    except ImportError:
        pass
    _runner_env()  # importing amplpy put the module directories first on PATH


class _RunnerFinder:
    # Replaces ampl_notebook() whenever amplpy is imported, wherever that
    # happens: also after a %pip install of amplpy in the same cell, and on a
    # reload. It stays in sys.meta_path and only answers for "amplpy".
    def find_spec(self, name, path=None, target=None):
        if name != "amplpy":
            return None
        spec = _PathFinder.find_spec(name, path)
        if spec is None:  # not installed yet
            return None
        exec_module = spec.loader.exec_module

        def _exec(module):
            exec_module(module)  # if this fails, the next import is patched
            _runner_patch(module)

        spec.loader.exec_module = _exec
        return spec


_runner_env()
if {plain!r}:
    _sys.meta_path.insert(0, _RunnerFinder())
"""

PIP = re.compile(r"^([ \t]*)([%!]\s*pip\s+install\b.*)$")
# "HiGHS 1.15.1: ...", also with a build in parentheses: "XPRESS 10.0.0 (48.01.01): ..."
SOLVER_LINE = re.compile(
    r"^([A-Za-z][\w .\-]*?\s+v?\d[\w.\-]*(?:\s*\([\w.\-]*\))?)\s*:\s*(.+)$"
)
NUMBER = r"-?\d+(?:\.\d*)?(?:[eE][-+]?\d+)?"
OBJECTIVE = re.compile(rf"objective\s+({NUMBER})")
STATUS = re.compile(
    r"(?i)\b(optimal|infeasible|unbounded|limit|failure|error|"
    r"locally optimal|feasible solution|solved)\b"
)
OWN_LIMIT = re.compile(
    r"(?:lim:time|timelimit|timelim|time_limit|maxtime|TimeLimit)\s*=\s*"
    rf"({NUMBER})"
)
# a solve in a cell: `solve;` in AMPL, ampl.solve(...) in Python
SOLVE = re.compile(r"\bsolve\s*[(;]")
# printed by notebooks that use generated data instead of downloaded data
SYNTHETIC = "Using synthetic data"
# objective values differing by less are not reported (--rel-tol): interior
# point and conic solvers move them by about 1e-6 between versions
REL_TOL = 1e-5
RANDOM = re.compile(r"\brandom\b|\brandint\b|np\.random|Uniform|Normal\(")
STATE = {"active": {}, "lock": threading.Lock(), "stop": False}


# ---- worker: executes one notebook (python run_notebooks.py --worker ...) ----


def comment_out_pip(source):
    """Comment out the `%pip install` and `!pip install` lines, with their
    continuation lines (ending in a backslash). An indented one becomes a
    `pass` statement: it may be the only statement of a block."""
    lines, continued = [], False
    for line in source.split("\n"):
        m = None if continued else PIP.match(line)
        if m:
            indent = m.group(1)
            stmt = "pass  " if indent else ""
            lines.append(f"{indent}{stmt}# (runner) {m.group(2)}")
        elif continued:
            lines.append(f"# (runner) {line}")
        else:
            lines.append(line)
        continued = (bool(m) or continued) and line.rstrip().endswith("\\")
    return "\n".join(lines)


def kernel_manager_class():
    """A kernel manager that starts the kernel with this worker's interpreter
    (--python). Asked for "python3", Jupyter would prefer a kernelspec of that
    name installed in the user or system folders, which may run another
    Python, over ipykernel's own one."""
    from jupyter_client.kernelspec import KernelSpec
    from jupyter_client.manager import AsyncKernelManager

    spec = KernelSpec(
        argv=[sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
        display_name="Python 3 (run_notebooks.py)",
        language="python",
    )

    class Manager(AsyncKernelManager):
        @property
        def kernel_spec(self):
            return spec

    return Manager


def execute(src, dst, cell_timeout, prefix, licfile, plain, skip_pip):
    import nbformat
    from nbclient import NotebookClient
    from nbclient.exceptions import CellExecutionError, CellTimeoutError

    nb = nbformat.read(src, as_version=4)
    for cell in nb.cells:
        if cell.cell_type == "code":
            if skip_pip:
                cell.source = comment_out_pip(cell.source)
            cell.outputs = []
    code = PRELUDE.format(prefix=prefix, licfile=licfile, plain=plain)
    nb.cells.insert(0, nbformat.v4.new_code_cell(code))
    path = os.path.dirname(os.path.abspath(src))
    client = NotebookClient(
        nb,
        timeout=cell_timeout,
        kernel_name="python3",
        kernel_manager_class=kernel_manager_class(),
        resources={"metadata": {"path": path}},
    )
    started = {}  # index of the last cell started, with the prelude in front
    client.on_cell_start = lambda cell, cell_index: started.update(i=cell_index)
    t0, info = time.time(), {"status": "ok"}
    try:
        client.execute()
    except CellTimeoutError:
        info["status"] = "cell_timeout"
    except CellExecutionError:
        info["status"] = "error"
    except Exception as e:
        info["status"] = "runner_error"
        info["error"] = {"ename": type(e).__name__, "evalue": str(e)[:400]}
    if info["status"] != "ok" and "i" in started:
        info["cell"] = started["i"] - 1  # cell number of the original notebook
    info["seconds"] = round(time.time() - t0, 1)
    nb.metadata["notebook_runner"] = info
    nbformat.write(nb, dst)  # read_notebook() tolerates a truncated file


# ---- comparison with the stored outputs ----


def outputs_text(cell):
    """The text of a cell's outputs: streams are joined as written (a line
    may be split over several stream outputs), other outputs are put on
    lines of their own."""
    result = ""
    for out in cell.get("outputs", []):
        if out.get("output_type") == "stream":
            text = out.get("text", "")
            result += "".join(text) if isinstance(text, list) else str(text)
            continue
        if out.get("output_type") == "error":
            text = f"{out.get('ename')}: {out.get('evalue')}"
        else:
            text = out.get("data", {}).get("text/plain", "")
            text = "".join(text) if isinstance(text, list) else str(text)
        if result and not result.endswith("\n"):
            result += "\n"
        result += text + "\n"
    return result


def solver_messages(nb, offset=0):
    """{cell: [(status, objective, line)]} of the solver headlines, with the
    cell numbers of the original notebook (offset: cells added in front)."""
    messages, warnings = {}, set()
    for i, cell in enumerate(nb.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue
        for line in outputs_text(cell).splitlines():
            line = line.split("\b")[-1].strip()
            m = SOLVER_LINE.match(line)
            if m and STATUS.search(m.group(2)):
                obj = OBJECTIVE.search(m.group(2))
                status = STATUS.search(m.group(2)).group(1).lower()
                value = float(obj.group(1).rstrip(".")) if obj else None
                messages.setdefault(i - offset, []).append((status, value, line[:160]))
            if "WARNING" in line or "Warning:" in line:
                warnings.add(line[:160])
    return messages, warnings


def compare_cell(cell, old, new, rel_tol=REL_TOL):
    if len(old) != len(new):
        line = (new or old)[0][2]
        return [f"cell {cell}: {len(old)} -> {len(new)} solves ({line})"]
    diffs = []
    for a, b in zip(old, new):
        if a[0] != b[0]:
            diffs.append(f"cell {cell}: '{a[2]}' -> '{b[2]}'")
        elif a[1] is not None and b[1] is not None:
            if abs(a[1] - b[1]) > rel_tol * max(1.0, abs(a[1])):
                diffs.append(
                    f"cell {cell}: objective {a[1]:.10g} -> {b[1]:.10g} ('{b[2]}')"
                )
    return diffs


def code_text(nb):
    return "\n".join(
        "".join(c.get("source", []))
        for c in nb.get("cells", [])
        if c.get("cell_type") == "code"
    )


def compare(orig, new, rel_tol=REL_TOL):
    """Solver headlines compared cell by cell, in the cells that have stored
    outputs and, after an error, up to the failed cell only. Objective values
    differ when they differ by more than rel_tol relative (absolute for values
    below 1 in magnitude)."""
    old_msgs, old_warn = solver_messages(orig)
    new_msgs, new_warn = solver_messages(new, offset=1)
    last = failed_cell(new)
    if last is None:
        last = len(orig.get("cells", []))
    stored = {
        i
        for i, c in enumerate(orig.get("cells", []))
        if c.get("cell_type") == "code" and c.get("outputs") and i <= last
    }
    diffs = []
    for cell in sorted((set(old_msgs) | set(new_msgs)) & stored):
        old, new_ = old_msgs.get(cell, []), new_msgs.get(cell, [])
        diffs += compare_cell(cell, old, new_, rel_tol)
    code = code_text(orig)
    return {
        "solves_old": sum(map(len, old_msgs.values())),
        "solves_new": sum(map(len, new_msgs.values())),
        "diffs": diffs,
        "new_warnings": sorted(new_warn - old_warn)[:10],
        "random_data": bool(RANDOM.search(code)) and "seed" not in code,
        "synthetic_data": any(
            SYNTHETIC in outputs_text(c) for c in new.get("cells", [])
        ),
    }


def failed_cell(nb):
    """Cell number (of the original notebook) where the run stopped, from the
    runner's metadata (also for a timeout, which adds no error output); None
    if the notebook ran to the end. Errors of cells tagged raises-exception
    do not stop the run."""
    info = nb.get("metadata", {}).get("notebook_runner", {})
    if info.get("status") == "ok":
        return None
    if "cell" in info:
        return info["cell"]
    error = first_error(nb)  # no metadata: the worker did not finish
    return error["cell"] if error else None


def first_error(nb, cell=None):
    """The first error output, of the given cell if one is given, with the
    cell number of the original notebook (the executed notebook has the
    prelude cell in front)."""
    for i, c in enumerate(nb.get("cells", [])):
        if cell is not None and i - 1 != cell:
            continue
        for out in c.get("outputs", []):
            if out.get("output_type") == "error":
                evalue = str(out.get("evalue"))[:400]
                return {"cell": i - 1, "ename": out.get("ename"), "evalue": evalue}
    return None


# ---- watchdog ----


def tree_rss(proc, seen):
    """RSS of proc and its descendants; adds the descendants to seen."""
    import psutil

    try:
        procs = [proc, *proc.children(recursive=True)]
    except psutil.NoSuchProcess:
        return 0
    except psutil.Error:  # AccessDenied on a child: measure the worker alone
        procs = [proc]
    seen.update(procs)
    total = 0
    for p in procs:
        try:
            total += p.memory_info().rss
        except psutil.Error:
            pass
    return total


def kill_all(procs):
    """Kill the processes still running. A killed Jupyter kernel leaves its
    children (AMPL, solvers) to the init process, outside the tree: hence all
    processes ever seen in the tree."""
    import psutil

    for p in procs:
        try:
            if p.is_running():
                p.kill()
        except psutil.Error:
            pass


def stop_reason(name, args, rss, elapsed, nb_timeout):
    import psutil

    with STATE["lock"]:
        STATE["active"][name] = rss
        largest = max(STATE["active"], key=STATE["active"].get)
    if STATE["stop"]:
        return "interrupted"
    if elapsed > nb_timeout:
        return "nb_timeout"
    if rss > args.mem_gb * 2**30:
        return "memory_limit"
    reserve = args.reserve_gb * 2**30
    if psutil.virtual_memory().available < reserve and largest == name:
        return "memory_guard"
    return None


def watch(popen, name, args, nb_timeout):
    """Wait for the notebook process; return (reason it was stopped, peak RSS).
    Afterwards, kill whatever the notebook left running."""
    import psutil

    try:
        proc = psutil.Process(popen.pid)
    except psutil.NoSuchProcess:  # the worker has already ended
        proc = None
    seen = set()
    t0, peak, reason = time.time(), 0, None
    try:
        while popen.poll() is None:
            rss = tree_rss(proc, seen) if proc else 0
            peak = max(peak, rss)
            reason = stop_reason(name, args, rss, time.time() - t0, nb_timeout)
            if reason:
                break
            time.sleep(1.0)
    finally:  # also when the loop raised: leave nothing running unwatched
        if popen.poll() is None:
            popen.kill()
        if proc:
            kill_all([proc, *seen])
        popen.wait()
    return reason, peak


# ---- driver ----


def strip_comment(line):
    """The line without a `#` comment (Python and AMPL), outside quotes."""
    quote, escaped = None, False
    for i, ch in enumerate(line):
        if escaped:
            escaped = False
        elif ch == "\\":
            escaped = True
        elif quote:
            quote = None if ch == quote else quote
        elif ch in "'\"":
            quote = ch
        elif ch == "#":
            return line[:i]
    return line


def cell_limits(nb):
    """The solver time limit of each code cell that may run a time-limited
    solve: in a cell that sets limits, the largest of them (one cell usually
    runs one solve; a solver and its MP2NL wrapper often repeat the same
    limit); in a later cell that solves (`solve;` or `solve(` in its code),
    the largest limit set so far, as an option set once applies to the later
    solves.
    Outside comments; only literal values are seen."""
    limits, so_far = [], None
    for c in nb.get("cells", []):
        if c.get("cell_type") != "code":
            continue
        lines = "".join(c.get("source", [])).splitlines()
        code = "\n".join(strip_comment(x) for x in lines)
        own = [float(x.rstrip(".")) for x in OWN_LIMIT.findall(code)]
        if own:
            limits.append(max(own))
            so_far = max(own) if so_far is None else max(so_far, max(own))
        elif so_far is not None and SOLVE.search(code):
            limits.append(so_far)
    return limits


def timeouts(path, args):
    """Cell and notebook timeouts. A notebook's own solver time limits raise
    them: the cell timeout to the largest limit times 1.3 plus 60 s, the
    notebook timeout to the sum of that over the cells, and to at least twice
    the cell timeout. The options are kept otherwise."""
    with open(path, encoding="utf-8") as f:
        limits = [int(1.3 * x + 60) for x in cell_limits(json.load(f))]
    if not limits:
        return args.cell_timeout, args.nb_timeout
    cell = max(args.cell_timeout, max(limits))
    return cell, max(args.nb_timeout, 2 * cell, sum(limits))


def worker_env(args):
    env = dict(os.environ)
    if args.licfile:
        env["AMPL_LICFILE"] = args.licfile
    if args.synthetic_data:
        env["COLAB_SYNTHETIC_DATA"] = "1"
    try:
        import certifi

        env.setdefault("SSL_CERT_FILE", certifi.where())
    except ImportError:
        pass
    return env


def prepare(name, args):
    """Fresh copy of the notebook's folder; returns (src, dst). Results of an
    earlier run of the notebook are removed first."""
    work = os.path.join(args.out, "work", name[: -len(".ipynb")])
    dst = os.path.join(args.out, "executed", name)
    shutil.rmtree(work, ignore_errors=True)
    for path in (dst, dst + ".log"):
        if os.path.exists(path):
            os.remove(path)
    shutil.copytree(
        os.path.dirname(os.path.join(ROOT_DIR, name)),
        work,
        # other notebooks and editor copies
        ignore=shutil.ignore_patterns(
            ".virtual_documents", ".ipynb_checkpoints", "*.ipynb"
        ),
    )
    src = os.path.join(work, os.path.basename(name))
    shutil.copy(os.path.join(ROOT_DIR, name), src)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    return src, dst


def run_one(name, args):
    if STATE["stop"]:
        return
    t0 = time.time()
    try:
        src, dst = prepare(name, args)
        cell_timeout, nb_timeout = timeouts(src, args)
        prefix = os.pathsep.join(args.bin_dir)
        cmd = [args.python, os.path.abspath(__file__), "--worker", src, dst]
        cmd += [str(cell_timeout), prefix, args.licfile or ""]
        cmd += ["1" if args.bin_dir else "", "1" if args.skip_pip else ""]
        with open(dst + ".log", "w") as log:
            popen = subprocess.Popen(
                cmd,
                cwd=os.path.dirname(src),
                stdout=log,
                stderr=subprocess.STDOUT,
                env=worker_env(args),
                start_new_session=True,  # signals go to the runner only
            )
            stopped, peak = watch(popen, name, args, nb_timeout)
        with STATE["lock"]:
            STATE["active"].pop(name, None)
        # after Ctrl+C or SIGTERM, a notebook that ended meanwhile (its kernel
        # may have been killed with the runner's process tree) is not recorded
        if stopped != "interrupted" and not STATE["stop"]:
            record(name, args, stopped, peak, round(time.time() - t0, 1), dst)
    except Exception as e:  # one notebook must not stop the run
        with STATE["lock"]:
            STATE["active"].pop(name, None)
        error = {"ename": type(e).__name__, "evalue": str(e)[:400]}
        write_record(
            {
                "notebook": name,
                "status": "runner_error",
                "seconds": 0,
                "peak_rss_gb": 0,
                "error": error,
            },
            args,
        )


def record(name, args, stopped, peak, seconds, dst):
    rec = {"notebook": name, "seconds": seconds, "peak_rss_gb": round(peak / 2**30, 2)}
    new = read_notebook(dst)
    if new is not None:
        with open(os.path.join(ROOT_DIR, name), encoding="utf-8") as f:
            orig = json.load(f)
        info = new.get("metadata", {}).get("notebook_runner", {})
        rec["status"] = info.get("status")
        rec["error"] = run_error(new, info)
        rec.update(compare(orig, new, args.rel_tol))
    else:
        with open(dst + ".log") as f:
            rec["error"] = {"ename": "log", "evalue": f.read()[-400:]}
    rec["status"] = stopped or rec.get("status") or "no_output"
    write_record(rec, args)


def run_error(nb, info):
    """The error output of the cell where the run stopped; otherwise the
    runner's error (a dead kernel) or the stopped cell (a timeout), with the
    cell number. None after a run to the end: errors of cells tagged
    raises-exception are part of the notebook."""
    if info.get("status") == "ok":
        return None
    error = first_error(nb, info.get("cell")) or info.get("error")
    if error is None and "cell" in info:
        error = {"ename": info["status"], "evalue": ""}
    if error is not None and "cell" in info:
        error.setdefault("cell", info["cell"])
    return error


def read_notebook(path):
    """The executed notebook, or None if it is missing or unreadable."""
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def write_record(rec, args):
    path = os.path.join(args.out, "results.jsonl")
    with STATE["lock"], open(path, "a+b") as f:
        if f.seek(0, os.SEEK_END):  # end a line cut short: keep this one apart
            f.seek(-1, os.SEEK_END)
            if f.read(1) != b"\n":
                f.write(b"\n")
        f.write((json.dumps(rec) + "\n").encode())
    print(
        f"{rec['status']:13s} {rec['seconds']:7.1f}s {rec['peak_rss_gb']:5.2f}GB "
        f"diffs={len(rec.get('diffs', []))} {rec['notebook']}",
        flush=True,
    )


def error_text(err):
    cell = err.get("cell")
    where = "prelude: " if cell == -1 else "" if cell is None else f"cell {cell}: "
    text = f"{where}{err.get('ename')}"
    return f"{text}: {err['evalue']}" if err.get("evalue") else text


def describe(rec):
    err = rec.get("error") or {}
    parts = []
    if rec.get("random_data"):
        parts.append("(random data without seed)")
    if rec.get("synthetic_data"):
        parts.append("(synthetic data)")
    if err and (rec["status"] != "ok" or not rec.get("diffs")):
        parts.append(error_text(err))
    parts += rec.get("diffs", [])[:3]
    if rec.get("new_warnings"):
        parts.append("new warnings: " + "; ".join(rec["new_warnings"][:2]))
    return "; ".join(parts).replace("|", "/").replace("\n", " ")[:300]


def read_results(out):
    """The records of results.jsonl. A line that cannot be read (cut short
    when the runner was killed while writing it) is skipped with a warning:
    its notebook runs again."""
    path = os.path.join(out, "results.jsonl")
    if not os.path.exists(path):
        return []
    recs = []
    with open(path) as f:
        for number, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                recs.append(json.loads(line))
            except ValueError:
                print(f"{path}:{number}: unreadable line skipped", file=sys.stderr)
    return recs


def summary(out):
    recs = read_results(out)
    try:
        with open(os.path.join(out, "not_found.json")) as f:
            not_found = json.load(f)
    except (OSError, ValueError):
        not_found = []
    lines = ["# Notebook run", "", f"{len(recs)} notebooks", ""]
    if not_found:
        lines += ["Not notebooks of the repository: " + ", ".join(not_found), ""]
    for status in sorted({r["status"] for r in recs}):
        count = sum(r["status"] == status for r in recs)
        lines.append(f"- {status}: {count}")
    lines += [
        "",
        "| Notebook | Status | s | GB | Solves stored/new | Differences or error |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    order = sorted(recs, key=lambda r: (r["status"] == "ok" and not r.get("diffs"),))
    for r in order:
        lines.append(
            f"| {r['notebook']} | {r['status']} | {r['seconds']} | "
            f"{r['peak_rss_gb']} | {r.get('solves_old', '')}/"
            f"{r.get('solves_new', '')} | {describe(r)} |"
        )
    with open(os.path.join(out, "summary.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    return recs


def recompare(out, rel_tol=REL_TOL):
    if not os.path.isdir(out):
        sys.exit(f"no results folder {out}")
    recs = read_results(out)
    for rec in recs:
        new = read_notebook(os.path.join(out, "executed", rec["notebook"]))
        orig = read_notebook(os.path.join(ROOT_DIR, rec["notebook"]))
        if orig is None:
            print(f"kept as it was: {rec['notebook']} is no longer in the repository")
        elif new is not None:
            rec.update(compare(orig, new, rel_tol))
    with open(os.path.join(out, "results.jsonl"), "w") as f:
        f.writelines(json.dumps(r) + "\n" for r in recs)
    summary(out)


def repo_path(path):
    """The notebook path relative to the repository root (paths are taken
    relative to the current folder), or None if it is not a notebook of the
    repository."""
    try:
        rel = os.path.relpath(os.path.realpath(path), ROOT_DIR)
    except ValueError:  # another drive on Windows
        return None
    if rel == os.pardir or rel.startswith(os.pardir + os.sep):
        return None
    if not rel.endswith(".ipynb"):
        return None
    if not os.path.isfile(os.path.join(ROOT_DIR, rel)):
        return None
    return rel.replace(os.sep, "/")


def notebooks(args):
    """The notebooks given as arguments and in the --list file; without
    either, the notebooks that CI runs."""
    names = list(args.notebooks)
    if args.list:
        with open(args.list) as f:
            lines = (x.strip() for x in f)
            names += [x for x in lines if x and not x.startswith("#")]
    if args.notebooks or args.list:
        return names
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from list_notebooks import list_notebooks

    cwd = os.getcwd()
    os.chdir(ROOT_DIR)
    try:
        return [os.path.join(ROOT_DIR, n) for n in list_notebooks()]
    finally:
        os.chdir(cwd)


def parse_args():
    ap = argparse.ArgumentParser(
        description=__doc__.split("\n\n")[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument(
        "notebooks",
        nargs="*",
        help="notebook paths (default: the notebooks that CI runs)",
    )
    ap.add_argument(
        "--list", help="file with notebook paths, one per line (added to the paths)"
    )
    ap.add_argument(
        "--out",
        default=os.path.join(ROOT_DIR, "notebook-runs", "latest"),
        help="results folder (default: notebook-runs/latest in the repository)",
    )
    ap.add_argument("--jobs", type=int, default=2, help="notebooks run in parallel")
    ap.add_argument("--cell-timeout", type=int, default=180, help="seconds")
    ap.add_argument("--nb-timeout", type=int, default=600, help="seconds")
    ap.add_argument("--mem-gb", type=float, default=5, help="per notebook (RSS)")
    ap.add_argument("--reserve-gb", type=float, default=2.5, help="free memory kept")
    ap.add_argument(
        "--bin-dir",
        action="append",
        default=[],
        help="directory with AMPL or solver executables, put first on PATH "
        "(repeatable); ampl_notebook() then only creates AMPL()",
    )
    ap.add_argument("--licfile", help="AMPL license file (AMPL_LICFILE)")
    ap.add_argument("--skip-pip", action="store_true", help="comment out %%pip lines")
    ap.add_argument(
        "--synthetic-data",
        action="store_true",
        help="set COLAB_SYNTHETIC_DATA=1: generated data instead of downloads",
    )
    ap.add_argument("--python", default=sys.executable, help="Python for the kernels")
    ap.add_argument("--recompare", action="store_true", help="only redo the summary")
    ap.add_argument(
        "--rel-tol",
        type=float,
        default=REL_TOL,
        help="objective values differing by less are the same: relative, "
        f"absolute below 1 in magnitude (default {REL_TOL:g})",
    )
    ap.add_argument(
        "--fail-on-diff",
        action="store_true",
        help="exit code 1 also when solver results differ from the stored "
        "outputs (except with synthetic data)",
    )
    return ap.parse_args()


def absolute_args(args):
    """The worker runs in the notebook's folder copy: make paths absolute."""
    args.out = os.path.abspath(args.out)
    args.bin_dir = [os.path.abspath(d) for d in args.bin_dir]
    if args.licfile:
        args.licfile = os.path.abspath(args.licfile)
    if os.sep in args.python or (os.altsep and os.altsep in args.python):
        args.python = os.path.abspath(args.python)
    else:
        args.python = shutil.which(args.python) or args.python


def stop_on_signals():
    """SIGTERM and SIGHUP (a closed terminal) stop the run like Ctrl+C: the
    workers run in sessions of their own and would not get them."""

    def handler(signum, frame):
        raise KeyboardInterrupt

    for name in ("SIGTERM", "SIGHUP"):
        if hasattr(signal, name):
            signal.signal(getattr(signal, name), handler)


def refuse_out_in_folders(out, names):
    """Each notebook's folder is copied into OUT/work: OUT must not lie in it."""
    out = os.path.realpath(out)
    for name in names:
        folder = os.path.realpath(os.path.dirname(os.path.join(ROOT_DIR, name)))
        if out == folder or out.startswith(folder + os.sep):
            print(f"--out {out} is inside the folder of {name}", file=sys.stderr)
            sys.exit(2)


def refuse_out_in_repository(out):
    """OUT/executed holds copies of the notebooks: inside the repository, only
    notebook-runs/ is skipped by list_notebooks.py, check_headers.py and
    index.py, and ignored by git."""
    out = os.path.realpath(out)
    root = os.path.realpath(ROOT_DIR)
    runs = os.path.join(root, "notebook-runs")
    inside = out == root or out.startswith(root + os.sep)
    if inside and not (out == runs or out.startswith(runs + os.sep)):
        print(
            f"--out {out} is in the repository: use a folder in notebook-runs/ "
            "or outside the repository",
            file=sys.stderr,
        )
        sys.exit(2)


def run_all(names, args):
    """Run the notebooks; on Ctrl+C, stop the running ones without recording
    them, so that a rerun with the same --out runs them again. Signals are
    ignored afterwards: the cleanup and the summary must finish."""
    ex = ThreadPoolExecutor(args.jobs)
    try:
        futures = [ex.submit(run_one, n, args) for n in names]
        for f in futures:
            f.result()
    except KeyboardInterrupt:
        STATE["stop"] = True
        ignore_signals()
        print("interrupted: stopping the running notebooks", flush=True)
    finally:
        ignore_signals()
        ex.shutdown(wait=True, cancel_futures=True)


def ignore_signals():
    for name in ("SIGINT", "SIGTERM", "SIGHUP"):
        if hasattr(signal, name):
            signal.signal(getattr(signal, name), signal.SIG_IGN)


def main():
    if sys.argv[1:2] == ["--worker"]:
        src, dst, timeout, prefix, licfile, plain, skip_pip = sys.argv[2:9]
        execute(src, dst, int(timeout), prefix, licfile, bool(plain), bool(skip_pip))
        return
    args = parse_args()
    absolute_args(args)
    if args.recompare:
        recompare(args.out, args.rel_tol)
        return
    try:
        import psutil  # noqa: F401
    except ImportError:
        # without it, a stopped kernel would leave AMPL and solvers running
        print("psutil is required: pip install psutil", file=sys.stderr)
        sys.exit(2)
    done = {r["notebook"] for r in read_results(args.out)}
    todo, bad = [], []
    for given in notebooks(args):
        name = repo_path(given)
        if name is None:
            bad.append(given)
        elif name not in done and name not in todo:
            todo.append(name)
    refuse_out_in_folders(args.out, todo)
    refuse_out_in_repository(args.out)
    os.makedirs(args.out, exist_ok=True)
    for given in bad:
        print(f"not_found     {given}: not a notebook of the repository")
    with open(os.path.join(args.out, "not_found.json"), "w") as f:
        json.dump(bad, f)
    print(f"{len(todo)} notebooks to run ({len(done)} done), jobs={args.jobs}")
    stop_on_signals()
    run_all(todo, args)
    recs = summary(args.out)
    if STATE["stop"]:
        sys.exit(130)
    ok = not bad and all(r["status"] == "ok" for r in recs)
    if args.fail_on_diff:
        ok = ok and not any(
            r.get("diffs") and not r.get("synthetic_data") for r in recs
        )
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
