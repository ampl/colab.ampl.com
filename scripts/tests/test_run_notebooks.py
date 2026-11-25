"""Tests of scripts/run_notebooks.py.

Most tests copy the script into a temporary repository, write small notebooks
there and run the script on them, so the real repository is not changed. The
notebooks print solver headlines instead of solving, and the --bin-dir tests
use a stub amplpy package: no AMPL, solver, license or amplpy is needed. The
last tests call functions of the script directly. Requires pytest, nbclient,
nbformat and ipykernel, and psutil for the interruption test.

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
        self.option = {"ampl_libpath": "", "version": "AMPL stub\\nLicensed"}


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


@pytest.mark.parametrize("same_cell", [False, True], ids=["pip_cell", "same_cell"])
def test_bin_dir_replaces_ampl_notebook(repo, tmp_path, same_cell):
    """With --bin-dir, ampl_notebook() is replaced also when amplpy is
    installed only by the notebook (in an earlier cell, or in the same cell as
    in template/minimal.ipynb), and the --bin-dir folders stay first on PATH."""
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
    cells = (
        [(install + "\n" + use, None)] if same_cell else [(install, None), (use, None)]
    )
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
    show = "import os\nprint(os.environ['PATH'].split(os.pathsep)[0])"
    nb = write_notebook(repo, "path.ipynb", [(show, None)])
    _, out = run(repo, nb, "--bin-dir", str(bin_dir), env={"PYTHONPATH": str(stub)})
    executed = nbformat.read(os.path.join(out, "executed", nb), as_version=4)
    assert executed.cells[-1].outputs[0]["text"].strip() == str(bin_dir)


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
        "# opt = 'lim:time=1000'  (a comment: ignored)\nopt = 'lim:time=30'",
        "opt = 'lim:time=300 maxtime=300'",  # one solve: counted once
        "opt = 'lim:time=300'",
    ]
    nb.cells = [nbformat.v4.new_code_cell(s) for s in sources]
    path = tmp_path / "limits.ipynb"
    nbformat.write(nb, path)
    args = types.SimpleNamespace(cell_timeout=180, nb_timeout=600)
    # cells: 1.3 * 30 + 60 = 99, 1.3 * 300 + 60 = 450 twice
    assert runner.timeouts(path, args) == (450, 999)


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
    """Relative 1e-6, absolute 1e-6 below 1 in magnitude (as in TESTING.md)."""
    runner = load_runner()
    assert (
        runner.compare_cell(0, [("optimal", 1e-8, "")], [("optimal", 5e-8, "")]) == []
    )
    assert runner.compare_cell(0, [("optimal", 1e3, "")], [("optimal", 1.01e3, "")])


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
