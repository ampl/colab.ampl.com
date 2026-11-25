"""Tests of scripts/run_notebooks.py with small notebooks written by the tests.

Each test copies the script into a temporary repository and runs it there, so
the real repository is not changed. The notebooks print solver headlines
instead of solving: no AMPL or solver is needed. Requires pytest, nbclient,
nbformat, ipykernel and psutil; the --bin-dir test also needs amplpy (no
modules, no license).

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
psutil = pytest.importorskip("psutil")

SCRIPT = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "run_notebooks.py"
)
SOLVED = "HiGHS 1.15.1: optimal solution; objective 1\n"
# ignores SIGINT like AMPL during a solve: no KeyboardInterrupt on a timeout
SLEEP_IGNORING_SIGINT = (
    "import signal, time\nsignal.signal(signal.SIGINT, signal.SIG_IGN)\ntime.sleep(60)"
)


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


def run(repo, *args, out=None, env=None, timeout=120):
    out = out or repo.parent / "out"
    cmd = [sys.executable, "scripts/run_notebooks.py", "--out", str(out), *args]
    proc = subprocess.run(
        cmd,
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


def test_bin_dir_patches_ampl_notebook_installed_later(repo, tmp_path):
    """With --bin-dir, ampl_notebook() is replaced also when amplpy becomes
    importable only after the prelude, as after a notebook's %pip cell."""
    pytest.importorskip("amplpy")
    blocker = tmp_path / "blocker"
    (blocker / "amplpy").mkdir(parents=True)
    (blocker / "amplpy" / "__init__.py").write_text("raise ImportError('blocked')\n")
    nb = write_notebook(
        repo,
        "latepip.ipynb",
        [
            # "installs" amplpy: removes the blocker from the path
            (f"import sys\nsys.path.remove({str(blocker)!r})", None),
            ("from amplpy import ampl_notebook\nprint(ampl_notebook.__name__)", None),
        ],
    )
    _, out = run(repo, nb, "--bin-dir", str(tmp_path), env={"PYTHONPATH": str(blocker)})
    assert results(out)[nb]["status"] == "ok"
    executed = nbformat.read(os.path.join(out, "executed", nb), as_version=4)
    assert executed.cells[-1].outputs[0]["text"].strip() == "_runner_ampl_notebook"


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
    assert "cell 1: ValueError: boom" in summary(out)


def test_folder_copy_keeps_zip_files_and_skips_the_results(repo):
    with zipfile.ZipFile(repo / "authors" / "t" / "data.zip", "w") as z:
        z.writestr("a.txt", "1")
    nb = write_notebook(
        repo,
        "zip.ipynb",
        [("import zipfile\nprint(zipfile.ZipFile('data.zip').read('a.txt'))", None)],
    )
    out = repo / "authors" / "t" / "runs"  # inside the notebook's folder
    run(repo, nb, out=out)
    assert results(out)[nb]["status"] == "ok"
    assert not (out / "work" / "authors" / "t" / "zip" / "runs").exists()


def test_list_file_and_recompare(repo, tmp_path):
    nb = write_notebook(repo, "raises.ipynb", [("raise ValueError('boom')", None)])
    listing = tmp_path / "list.txt"
    listing.write_text(f"  # an indented comment\n{nb}\nmissing.ipynb\n")
    proc, out = run(repo, "--list", str(listing))
    assert "comment" not in proc.stdout
    assert list(results(out)) == [nb]
    assert "Not notebooks of the repository: missing.ipynb" in summary(out)
    os.remove(repo / nb)  # the notebook is gone before the recompare
    proc, _ = run(repo, "--recompare")
    assert proc.returncode == 0, proc.stderr
    assert "Not notebooks of the repository: missing.ipynb" in summary(out)
    assert list(results(out)) == [nb]


def test_interruption_records_nothing(repo):
    """Killing the runner's whole process tree, kernels included, must not
    record the running notebook: a rerun with the same --out runs it again."""
    nb = write_notebook(repo, "slow.ipynb", [("import time\ntime.sleep(60)", None)])
    out = repo.parent / "out"
    cmd = [sys.executable, "scripts/run_notebooks.py", "--out", str(out), nb]
    proc = subprocess.Popen(cmd, cwd=repo, stdout=subprocess.PIPE, text=True)
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
