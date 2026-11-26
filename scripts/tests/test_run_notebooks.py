"""Tests of scripts/run_notebooks.py.

Most tests copy the script into a temporary repository, write small notebooks
there and run the script on them, so the real repository is not changed. The
notebooks print solver headlines instead of solving, and the --bin-dir tests
use a stub amplpy package: no AMPL, solver, license or amplpy is needed. The
last tests call functions of the script directly. Requires pytest, nbclient,
nbformat, ipykernel and psutil.

From the repository root:

    python -m pytest scripts/tests
"""

import importlib.util
import json
import os
import shutil
import signal
import subprocess
import sys
import time
import types
import zipfile

import pytest

nbformat = pytest.importorskip("nbformat")
pytest.importorskip("nbclient")
pytest.importorskip("ipykernel")

SCRIPT = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "run_notebooks.py"
)
SOLVED = "HiGHS 1.15.1: optimal solution; objective 1\n"
# ignores SIGINT like AMPL during a solve: no KeyboardInterrupt on a timeout
SLEEP_IGNORING_SIGINT = (
    "import signal, time\nsignal.signal(signal.SIGINT, signal.SIG_IGN)\ntime.sleep(60)"
)
# A stub of amplpy: importing it puts a module folder first on PATH, as the
# real amplpy does with the installed modules; its ampl_notebook() must not be
# called with --bin-dir.
STUB_AMPLPY = """
import os

os.environ["PATH"] = "/stub/ampl_module_base/bin" + os.pathsep + os.environ["PATH"]


class AMPL:
    def __init__(self):
        # ampl_libpath unset: the replacement must not add to None
        self.option = {"ampl_libpath": None, "version": "AMPL stub\\nLicensed"}


def register_magics(**kwargs):
    pass


def ampl_notebook(**kwargs):
    raise RuntimeError("the real ampl_notebook() was called")
"""


def load_runner():
    spec = importlib.util.spec_from_file_location("run_notebooks", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def repo(tmp_path):
    """A repository with the script and an empty folder for notebooks."""
    root = tmp_path / "repo"
    (root / "scripts").mkdir(parents=True)
    shutil.copy(SCRIPT, root / "scripts")
    (root / "authors" / "t").mkdir(parents=True)
    return root


def write_notebook(repo, name, cells):
    """cells: (source, stored stdout or None) pairs."""
    nb = nbformat.v4.new_notebook()
    nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3"}
    for source, stored in cells:
        cell = nbformat.v4.new_code_cell(source)
        if stored:
            cell.outputs = [
                nbformat.v4.new_output("stream", name="stdout", text=stored)
            ]
        nb.cells.append(cell)
    nbformat.write(nb, repo / "authors" / "t" / name)
    return f"authors/t/{name}"


def command(repo, out, args):
    # no free-memory reserve: the result must not depend on the machine's load
    script = os.path.join(repo, "scripts", "run_notebooks.py")
    return [sys.executable, script, "--out", str(out), "--reserve-gb", "0", *args]


def run(repo, *args, out=None, env=None, timeout=120):
    out = out or repo.parent / "out"
    proc = subprocess.run(
        command(repo, out, args),
        check=False,
        cwd=repo,
        capture_output=True,
        text=True,
        timeout=timeout,
        env={**os.environ, **(env or {})},
    )
    return proc, out


def results(out):
    path = os.path.join(out, "results.jsonl")
    if not os.path.exists(path):
        return {}
    with open(path) as f:
        return {r["notebook"]: r for r in map(json.loads, f)}


def summary(out):
    with open(os.path.join(out, "summary.md")) as f:
        return f.read()


def test_cell_timeout_stops_the_comparison(repo):
    """A timed-out cell gets no error output from nbclient: the comparison must
    still stop there, and the summary must name the cell."""
    nb = write_notebook(
        repo,
        "timeout.ipynb",
        [
            (SLEEP_IGNORING_SIGINT, None),
            (f"print({SOLVED!r})", SOLVED),
            (f"print({SOLVED!r})", SOLVED),
        ],
    )
    _, out = run(repo, nb, "--cell-timeout", "3")
    rec = results(out)[nb]
    assert rec["status"] == "cell_timeout"
    assert rec["diffs"] == []
    assert rec["error"]["cell"] == 0
    assert "cell 0: cell_timeout" in summary(out)


@pytest.mark.parametrize("case", ["pip_cell", "same_cell", "failed_import_first"])
def test_bin_dir_replaces_ampl_notebook(repo, tmp_path, case):
    """With --bin-dir, ampl_notebook() is replaced also when amplpy is
    installed only by the notebook (in an earlier cell, or in the same cell as
    in template/minimal.ipynb, or after an import that failed), and the
    --bin-dir folders stay first on PATH."""
    blocker = tmp_path / "blocker" / "amplpy"  # amplpy not installed yet
    blocker.mkdir(parents=True)
    (blocker / "__init__.py").write_text("raise ImportError('not installed')\n")
    stub = tmp_path / "stub"
    (stub / "amplpy").mkdir(parents=True)
    (stub / "amplpy" / "__init__.py").write_text(STUB_AMPLPY)
    (stub / "ampl_module_plugins").mkdir()  # table handlers of the modules
    (stub / "ampl_module_plugins" / "__init__.py").write_text("")
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    install = (
        f"import sys\nsys.path.remove({str(blocker.parent)!r})\n"
        f"sys.path.insert(0, {str(stub)!r})  # as a %pip install"
    )
    use = (
        "import os\nfrom amplpy import ampl_notebook\n"
        "ampl = ampl_notebook(modules=['highs'], license_uuid='x')\n"
        "print('PATH0', os.environ['PATH'].split(os.pathsep)[0])\n"
        "print('LIBPATH', ampl.option['ampl_libpath'])"
    )
    cells = {
        "pip_cell": [(install, None), (use, None)],
        "same_cell": [(install + "\n" + use, None)],
        "failed_import_first": [
            ("try:\n    import amplpy\nexcept ImportError:\n    pass", None),
            (install, None),
            (use, None),
        ],
    }[case]
    nb = write_notebook(repo, "bindir.ipynb", cells)
    env = {"PYTHONPATH": str(blocker.parent)}
    _, out = run(repo, nb, "--bin-dir", str(bin_dir), env=env)
    rec = results(out)[nb]
    assert rec["status"] == "ok", rec.get("error")
    executed = nbformat.read(os.path.join(out, "executed", nb), as_version=4)
    text = "".join(o.get("text", "") for o in executed.cells[-1].outputs)
    lines = dict(x.split(" ", 1) for x in text.splitlines() if " " in x)
    assert lines["PATH0"] == str(bin_dir)
    assert lines["LIBPATH"] == os.path.join(str(stub), "ampl_module_plugins", "bin")


def test_bin_dir_first_on_path_with_amplpy_installed(repo, tmp_path):
    """With amplpy installed beforehand (as with --skip-pip), the --bin-dir
    folders come first on PATH also in the cells before ampl_notebook()."""
    stub = tmp_path / "stub"
    (stub / "amplpy").mkdir(parents=True)
    (stub / "amplpy" / "__init__.py").write_text(STUB_AMPLPY)
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    show = "import os\nimport amplpy\nprint(os.environ['PATH'].split(os.pathsep)[0])"
    nb = write_notebook(repo, "path.ipynb", [(show, None)])
    _, out = run(repo, nb, "--bin-dir", str(bin_dir), env={"PYTHONPATH": str(stub)})
    executed = nbformat.read(os.path.join(out, "executed", nb), as_version=4)
    assert executed.cells[-1].outputs[0]["text"].strip() == str(bin_dir)


def test_prelude_in_a_fresh_interpreter(tmp_path):
    """The import hook in a plain interpreter: no recursion in later imports
    (importlib.machinery not loaded yet), and a reload of amplpy keeps the
    replacement and the --bin-dir folder first on PATH."""
    stub = tmp_path / "stub"
    (stub / "amplpy").mkdir(parents=True)
    (stub / "amplpy" / "__init__.py").write_text(STUB_AMPLPY)
    code = f"""
import importlib, importlib.util, os, sys
spec = importlib.util.spec_from_file_location("rn", {SCRIPT!r})
rn = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rn)
prelude = rn.PRELUDE.format(prefix="/bin_dir", licfile="", plain="1")
sys.modules.pop("importlib.machinery", None)
exec(prelude, {{}})
import colorsys  # recursed when find_spec imported importlib.machinery
sys.path.insert(0, {str(stub)!r})
import amplpy
importlib.reload(amplpy)
print(amplpy.ampl_notebook.__name__, os.environ["PATH"].split(os.pathsep)[0])
"""
    proc = subprocess.run(
        [sys.executable, "-I", "-c", code], check=False, capture_output=True, text=True
    )
    assert proc.returncode == 0, proc.stderr[-2000:]
    assert proc.stdout.split() == ["_runner_ampl_notebook", "/bin_dir"]


def test_statuses_and_error_cells(repo):
    died = write_notebook(repo, "dies.ipynb", [("import os\nos._exit(1)", None)])
    raised = write_notebook(
        repo, "raises.ipynb", [("x = 1", None), ("raise ValueError('boom')", None)]
    )
    _, out = run(repo, died, raised)
    recs = results(out)
    assert recs[died]["status"] == "runner_error"  # plain, without the message
    assert recs[died]["error"]["ename"] == "DeadKernelError"
    assert recs[raised]["status"] == "error"
    assert "- runner_error: 1" in summary(out)
    assert "cell 0: DeadKernelError" in summary(out)
    assert "cell 1: ValueError: boom" in summary(out)


def test_folder_copy_keeps_zip_files(repo):
    with zipfile.ZipFile(repo / "authors" / "t" / "data.zip", "w") as z:
        z.writestr("a.txt", "1")
    nb = write_notebook(
        repo,
        "zip.ipynb",
        [("import zipfile\nprint(zipfile.ZipFile('data.zip').read('a.txt'))", None)],
    )
    _, out = run(repo, nb)
    assert results(out)[nb]["status"] == "ok"


@pytest.mark.parametrize("inside", ["", "runs"])
def test_out_in_a_notebook_folder_is_refused(repo, inside):
    """The folder would be copied into itself for each notebook."""
    nb = write_notebook(repo, "raises.ipynb", [("raise ValueError('boom')", None)])
    proc, out = run(repo, nb, out=repo / "authors" / "t" / inside)
    assert proc.returncode == 2
    assert "inside the folder of" in proc.stderr
    assert results(out) == {}


def test_out_in_the_repository_only_in_notebook_runs(repo):
    """Executed copies elsewhere in the repository would be taken for
    notebooks by list_notebooks.py, check_headers.py and index.py."""
    nb = write_notebook(repo, "ok.ipynb", [("x = 1", None)])
    proc, out = run(repo, nb, out=repo / "runs" / "today")
    assert proc.returncode == 2
    assert "is in the repository" in proc.stderr
    assert not out.exists()
    proc, out = run(repo, nb, out=repo / "notebook-runs" / "today")
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert list(results(out)) == [nb]


def test_unreadable_results_line_is_skipped(tmp_path, capsys):
    """A line cut short by a kill is skipped, and the next record is not
    appended to it."""
    runner = load_runner()
    (tmp_path / "results.jsonl").write_text('{"notebook": "a"}\n{"notebook": "b", "st')
    args = types.SimpleNamespace(out=str(tmp_path))
    rec = {"notebook": "c", "status": "ok", "seconds": 1.0, "peak_rss_gb": 0.0}
    runner.write_record(rec, args)
    assert [r["notebook"] for r in runner.read_results(str(tmp_path))] == ["a", "c"]
    assert "results.jsonl:2: unreadable line skipped" in capsys.readouterr().err


def test_synthetic_data(repo):
    """--synthetic-data sets COLAB_SYNTHETIC_DATA; a notebook that then prints
    the marker is marked in the summary, and its differences from the stored
    outputs do not fail --fail-on-diff."""
    other = SOLVED.replace("objective 1", "objective 2")
    source = (
        "import os\n"
        "if os.environ.get('COLAB_SYNTHETIC_DATA') == '1':\n"
        f"    print('Using synthetic data: ...'); print({other!r})\n"
        "else:\n"
        f"    print({SOLVED!r})\n"
    )
    nb = write_notebook(repo, "prices.ipynb", [(source, SOLVED)])
    proc, out = run(repo, nb, "--fail-on-diff", "--synthetic-data")
    rec = results(out)[nb]
    assert rec["synthetic_data"] and rec["diffs"], rec
    assert "(synthetic data)" in summary(out)
    assert proc.returncode == 0, proc.stdout + proc.stderr
    proc, out = run(repo, nb, "--fail-on-diff", out=repo.parent / "real")
    rec = results(out)[nb]
    assert not rec["synthetic_data"] and not rec["diffs"], rec
    assert proc.returncode == 0, proc.stdout + proc.stderr


def test_list_file_and_recompare(repo, tmp_path):
    nb = write_notebook(repo, "raises.ipynb", [("raise ValueError('boom')", None)])
    listing = tmp_path / "list.txt"
    listing.write_text(f"  # an indented comment\n{nb}\nmissing.ipynb\n")
    proc, out = run(repo, "--list", str(listing))
    assert "not_found     missing.ipynb" in proc.stdout
    assert "not_found     #" not in proc.stdout  # the comment is no path
    assert list(results(out)) == [nb]
    assert "Not notebooks of the repository: missing.ipynb" in summary(out)
    os.remove(repo / nb)  # the notebook is gone before the recompare
    proc, _ = run(repo, "--recompare")
    assert proc.returncode == 0, proc.stderr
    assert "Not notebooks of the repository: missing.ipynb" in summary(out)
    assert list(results(out)) == [nb]


def test_list_file_and_arguments_are_combined(repo, tmp_path):
    given = write_notebook(repo, "given.ipynb", [("x = 1", None)])
    listed = write_notebook(repo, "listed.ipynb", [("x = 2", None)])
    listing = tmp_path / "list.txt"
    listing.write_text(f"{listed}\n")
    proc, out = run(repo, given, "--list", str(listing))
    assert sorted(results(out)) == sorted([given, listed]), proc.stdout
    assert proc.returncode == 0, proc.stdout + proc.stderr


def test_raises_exception_cell_does_not_stop_the_comparison(repo):
    """nbclient runs on after a cell tagged raises-exception: the cells after
    it are compared, and its error is not reported as the run's error."""
    nb = nbformat.v4.new_notebook()
    nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3"}
    shown = nbformat.v4.new_code_cell("raise ValueError('shown')")
    shown.metadata["tags"] = ["raises-exception"]
    changed = SOLVED.replace("objective 1", "objective 2")
    later = nbformat.v4.new_code_cell(f"print({changed!r})")
    later.outputs = [nbformat.v4.new_output("stream", name="stdout", text=SOLVED)]
    nb.cells = [shown, later]
    nbformat.write(nb, repo / "authors" / "t" / "shown.ipynb")
    name = "authors/t/shown.ipynb"
    _, out = run(repo, name)
    rec = results(out)[name]
    assert rec["status"] == "ok", rec
    assert rec["error"] is None
    assert any("cell 1: objective 1 -> 2" in d for d in rec["diffs"]), rec


@pytest.mark.skipif(sys.platform == "win32", reason="SIGTERM is a hard kill there")
def test_second_sigterm_during_cleanup(repo):
    """A second SIGTERM while the running notebooks are stopped must not
    abort the cleanup: exit code 130 and a summary."""
    psutil = pytest.importorskip("psutil")
    nb = write_notebook(repo, "slow.ipynb", [("import time\ntime.sleep(60)", None)])
    out = repo.parent / "out"
    proc = subprocess.Popen(
        command(repo, out, [nb]),
        cwd=repo,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    runner = psutil.Process(proc.pid)
    deadline = time.time() + 60
    while len(runner.children(recursive=True)) < 2 and time.time() < deadline:
        time.sleep(0.2)  # wait for the worker and its kernel
    proc.send_signal(signal.SIGTERM)
    time.sleep(0.3)  # the watchdog checks once a second: still cleaning up
    proc.send_signal(signal.SIGTERM)
    stdout, stderr = proc.communicate(timeout=60)
    assert proc.returncode == 130, stdout + stderr
    assert "Traceback" not in stderr
    assert os.path.exists(out / "summary.md")


@pytest.mark.skipif(sys.platform == "win32", reason="SIGTERM is a hard kill there")
def test_interruption_records_nothing(repo):
    """Killing the runner's whole process tree, kernels included, must not
    record the running notebook: a rerun with the same --out runs it again."""
    psutil = pytest.importorskip("psutil")
    nb = write_notebook(repo, "slow.ipynb", [("import time\ntime.sleep(60)", None)])
    out = repo.parent / "out"
    proc = subprocess.Popen(
        command(repo, out, [nb]), cwd=repo, stdout=subprocess.PIPE, text=True
    )
    runner = psutil.Process(proc.pid)
    deadline = time.time() + 60
    while len(runner.children(recursive=True)) < 2 and time.time() < deadline:
        time.sleep(0.2)  # wait for the worker and its kernel
    time.sleep(2)
    for p in reversed([runner, *runner.children(recursive=True)]):
        try:
            p.send_signal(signal.SIGTERM)  # children first, as a tree kill may
        except psutil.NoSuchProcess:
            pass
    proc.communicate(timeout=60)
    assert proc.returncode == 130
    assert results(out) == {}


def test_notebook_timeout_sums_the_cell_limits(tmp_path):
    runner = load_runner()
    nb = nbformat.v4.new_notebook()
    sources = [
        (
            "# opt = 'lim:time=1000'  (a comment: ignored)\nopt = 'lim:time=30'"
            "  # was lim:time=36000 (a trailing comment: ignored)"
        ),
        "opt = 'gap=1e-4 # not a comment'  # lim:time=9999",
        "opt = 'lim:time=300 maxtime=300'",  # one solve: counted once
        "opt = 'lim:time=300'",
    ]
    nb.cells = [nbformat.v4.new_code_cell(s) for s in sources]
    path = tmp_path / "limits.ipynb"
    nbformat.write(nb, path)
    args = types.SimpleNamespace(cell_timeout=180, nb_timeout=600)
    # cells: 1.3 * 30 + 60 = 99, 1.3 * 300 + 60 = 450 twice
    assert runner.timeouts(path, args) == (450, 999)


def test_limit_set_once_counts_for_the_later_solves(tmp_path):
    """An option set once applies to every later solve."""
    runner = load_runner()
    nb = nbformat.v4.new_notebook()
    sources = [
        "ampl.solve()  # before any limit: not counted",
        "ampl.option['gurobi_options'] = 'timelimit=300'",
        *["ampl.solve()"] * 3,
        "%%ampl_eval\nsolve;",
        "print('no solve here')",
    ]
    nb.cells = [nbformat.v4.new_code_cell(s) for s in sources]
    path = tmp_path / "limits.ipynb"
    nbformat.write(nb, path)
    args = types.SimpleNamespace(cell_timeout=180, nb_timeout=600)
    # the cell that sets the limit and 4 solves: 5 * (1.3 * 300 + 60) = 2250
    assert runner.timeouts(path, args) == (450, 2250)


def test_skip_pip_keeps_valid_python():
    """Continuation lines are commented out too, and an indented %pip that is
    the only statement of a block becomes `pass`."""
    runner = load_runner()
    source = (
        "%pip install -q amplpy \\\n"
        "    pandas\n"
        "try:\n"
        "    !pip install numpy\n"
        "except Exception:\n"
        "    pass\n"
        "x = 1  # %pip install is not at the start: kept"
    )
    result = runner.comment_out_pip(source)
    compile(result, "cell", "exec")
    lines = result.split("\n")
    assert lines[0] == "# (runner) %pip install -q amplpy \\"
    assert lines[1] == "# (runner)     pandas"
    assert lines[3] == "    pass  # (runner) !pip install numpy"
    assert lines[6] == "x = 1  # %pip install is not at the start: kept"


def test_solver_headlines_with_a_build_number():
    runner = load_runner()

    def notebook(line):
        out = {"output_type": "stream", "name": "stdout", "text": line + "\n"}
        return {"cells": [{"cell_type": "code", "outputs": [out]}]}

    old = "XPRESS 9.8.0 (46.01.01): limit, feasible solution; objective 0.2696777839"
    new = "XPRESS 10.0.0 (48.01.01): locally optimal solution; objective 0.2672268893"
    a, _ = runner.solver_messages(notebook(old))
    b, _ = runner.solver_messages(notebook(new))
    assert a[0][0][:2] == ("limit", 0.2696777839)
    assert len(runner.compare_cell(0, a[0], b[0])) == 1


def test_objective_tolerance():
    """Relative 1e-5, absolute 1e-5 below 1 in magnitude (as in TESTING.md);
    --rel-tol changes it."""
    runner = load_runner()

    def diffs(a, b, *tol):
        return runner.compare_cell(0, [("optimal", a, "")], [("optimal", b, "")], *tol)

    assert diffs(1e-8, 5e-8) == []
    assert diffs(1e3, 1.01e3)
    # MOSEK 11.0.29 -> 11.2.0 in portfolio_factor_model.ipynb: round-off
    assert diffs(3.38248968, 3.382495447) == []
    assert diffs(3.38248968, 3.382495447, 1e-6)


def test_python_kernelspec_in_jupyter_folders_is_not_used(repo, tmp_path):
    """--python decides the kernel's interpreter, also when a "python3"
    kernelspec of another Python is installed in the Jupyter folders."""
    spec = tmp_path / "jupyter" / "kernels" / "python3"
    spec.mkdir(parents=True)
    argv = [
        "/nonexistent/python",
        "-m",
        "ipykernel_launcher",
        "-f",
        "{connection_file}",
    ]
    (spec / "kernel.json").write_text(
        json.dumps({"argv": argv, "display_name": "Other", "language": "python"})
    )
    nb = write_notebook(
        repo, "exe.ipynb", [("import sys\nprint(sys.executable)", None)]
    )
    proc, out = run(repo, nb, env={"JUPYTER_PATH": str(tmp_path / "jupyter")})
    assert results(out)[nb]["status"] == "ok", proc.stdout + proc.stderr
    executed = nbformat.read(out / "executed" / nb, as_version=4)
    assert executed.cells[1].outputs[0].text.strip() == sys.executable


def test_watch_kills_the_worker_when_it_raises(monkeypatch):
    """An error in the watch loop must not leave the notebook running."""
    psutil = pytest.importorskip("psutil")
    runner = load_runner()

    def fail(*args):
        raise psutil.AccessDenied()

    monkeypatch.setattr(runner, "stop_reason", fail)
    popen = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(60)"])
    try:
        with pytest.raises(psutil.AccessDenied):
            runner.watch(popen, "nb", None, 600)
        assert popen.poll() is not None
    finally:
        if popen.poll() is None:
            popen.kill()


def test_error_descriptions():
    runner = load_runner()

    def text(error):
        return runner.describe({"status": "error", "error": error})

    assert text({"cell": 2, "ename": "E", "evalue": "bad value:"}) == (
        "cell 2: E: bad value:"
    )
    assert text({"cell": 0, "ename": "cell_timeout", "evalue": ""}) == (
        "cell 0: cell_timeout"
    )
    assert text({"cell": -1, "ename": "E", "evalue": "x"}) == "prelude: E: x"
