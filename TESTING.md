# Testing the notebooks

There are three kinds of checks:

1. **CI** checks every push (`.github/workflows/test-notebooks.yml`).
2. **Checks before committing** run locally and are the same as in CI, apart from running
   the notebooks.
3. **Verification runs** with `scripts/run_notebooks.py` check the notebooks against new
   builds of AMPL or the solvers, for example before a release. You can also schedule them.

## 1. CI

On every push, CI runs these jobs:

- `scripts/check_headers.py` checks the header fields used by the website.
- `scripts/check_format.py` runs ruff in check mode.
- `python -m pytest scripts/tests` tests `scripts/run_notebooks.py` (see below).
- Every notebook listed by `scripts/list_notebooks.py` runs in its own job with
  `pytest --nbval-lax`, using the released AMPL and solvers from the amplpy modules.

A notebook passes when it runs without an exception. Most notebooks assert
`ampl.solve_result`, so a failed solve fails the job. `--nbval-lax` compares outputs only in
cells marked for it, so a changed objective value goes unnoticed.

`scripts/list_notebooks.py` skips some notebooks:

- those named in `SKIP_NB_LIST`;
- those that need credentials or external services (`SKIP_REGEX`);
- those that do not use amplpy;
- those under `venv`, `_build`, `build` and `notebook-runs`;
- copies in `.virtual_documents` and `.ipynb_checkpoints`.

To see the skipped ones, run `python scripts/list_notebooks.py --list-skipped`.

## 2. Before committing

From the repository root:

```bash
python scripts/check_headers.py   # header fields, as in CI
python scripts/check_format.py    # ruff check only, as in CI
python -m pytest scripts/tests    # tests of scripts/run_notebooks.py, as in CI
python scripts/index.py           # ruff fixes, headers and badges, README, docs index
git add docs/source/
```

`scripts/index.py` rewrites `README.md`, so edit the README text in `scripts/index.py`.

## 3. Verification runs: `scripts/run_notebooks.py`

Use this script when you need more than CI provides:

- to run with other AMPL or solver executables than the released modules (`--bin-dir`);
- to compare each solver result (status and objective value) with the output stored in the
  notebook;
- to run under a watchdog (time and memory limits) on a workstation, many notebooks at a
  time.

| | CI | `scripts/run_notebooks.py` |
| --- | --- | --- |
| AMPL and solvers | released amplpy modules | the modules, or executables given by `--bin-dir` |
| License | `amplpy.modules activate` with a secret | AMPL license file (`--licfile`) |
| Packages | `%pip install` cells of each notebook | the same, or preinstalled with `--skip-pip` |
| Downloaded data | downloaded; synthetic if the download fails | the same, or always synthetic with `--synthetic-data` |
| Pass criterion | no exception | no exception; solver results compared with the stored outputs |
| Limits | job timeout | per cell, per notebook, memory per notebook, free-memory reserve |
| Isolation | one job per notebook | one process tree and one copy of the notebook's folder per notebook |
| Results | job log | `results.jsonl`, `summary.md`, executed notebooks with logs |

### Setup

Use a virtual environment with Python 3.11 or later:

```bash
python -m venv venv-run
venv-run/bin/pip install amplpy nbclient nbformat ipykernel psutil certifi \
    pandas numpy matplotlib seaborn networkx scipy scikit-learn openpyxl ipywidgets
venv-run/bin/python -m amplpy.modules install highs gurobi coin plugins   # as needed
```

`psutil` is needed for the memory limits and for killing the processes that a notebook
leaves running. Without it, only the time limits apply, and the script says so when it
starts.

### Examples

```bash
# The notebooks that CI runs, with the released modules, two at a time
venv-run/bin/python scripts/run_notebooks.py --out notebook-runs/release \
    --licfile /path/to/ampl.lic

# Selected notebooks with other builds (directories put first on PATH, in this order)
venv-run/bin/python scripts/run_notebooks.py --list my_list.txt --out notebook-runs/build \
    --bin-dir /path/to/ampl --bin-dir /path/to/solvers --licfile /path/to/ampl.lic --skip-pip

# One notebook
venv-run/bin/python scripts/run_notebooks.py authors/lentz/gcg/bpp.ipynb --out notebook-runs/one

# Redo the comparison and the summary of a finished run
venv-run/bin/python scripts/run_notebooks.py --out notebook-runs/build --recompare
```

Notebook paths, given as arguments or in a list file, are absolute or relative to the
current folder (a path through a symbolic link works too), and must be inside the
repository. Other paths are reported as `not_found` when the run starts and in
`summary.md`, and make the exit code 1; they are not written to `results.jsonl` (but to
`not_found.json`, the paths of the last run, which `--recompare` reads). A list file has
one path per line; lines that start with `#`, after leading spaces, are comments.
`--out` must not lie in the folder of a notebook to run (the folder is copied into it);
the script refuses it with exit code 2. `--recompare` keeps the results of
notebooks that are no longer in the repository as they were.

A second run with the same `--out` skips the notebooks already in `results.jsonl`. To rerun
a notebook, delete its line from that file: its earlier results are removed when it runs
again. Ctrl+C, SIGTERM and SIGHUP (a closed terminal) stop the running notebooks without
recording them, so that the next run with the same `--out` runs them again. The notebooks
run in sessions of their own, so these signals reach them only through the script.

The exit code is 0 when every notebook has status `ok`, 1 otherwise, and 130 after Ctrl+C,
SIGTERM or SIGHUP.
With `--fail-on-diff`, differences from the stored outputs also give 1, except in notebooks
that used synthetic data.

Options (`--help` lists them all):

- `--jobs` (default 2) is the number of notebooks run in parallel.
- `--cell-timeout` (180 s), `--nb-timeout` (600 s), `--mem-gb` (5) and `--reserve-gb` (2.5)
  set the watchdog limits.
- `--python` sets the interpreter for the kernels; the default is the one that runs the
  script. The kernels are started with it directly: a `python3` kernelspec installed in the
  Jupyter folders (`jupyter kernelspec list`) is not used.
- `--rel-tol` (1e-5) is the tolerance for objective values in the comparison (see "Reading
  the comparison"). Interior point and conic solvers move objective values by about 1e-6
  between versions.
- `--out` is the results folder; the default is `notebook-runs/latest` in the repository.
- `--synthetic-data` sets `COLAB_SYNTHETIC_DATA=1`: the notebooks that download data
  generate it instead (see "Downloaded data" below), so the run needs no network access to
  the data sources and gives the same data every time.

### What it does

- **Copy.** Each notebook runs in a copy of its folder under `OUT/work`, so the repository
  is not changed. Notebooks of one folder that write the same files can therefore run in
  parallel.
- **Prelude cell.** A cell added in front puts the `--bin-dir` directories first on `PATH`
  and sets `AMPL_LICFILE`. With `--bin-dir`, it also makes `ampl_notebook()` only create
  `AMPL()` and register the magics: it installs no modules and activates no license.
  Whatever the notebook asks for in `modules=[...]` then comes from the given directories,
  or from the installed modules when a solver is not there. `ampl_notebook()` is replaced
  when amplpy is imported, so also when the notebook's own `%pip` installs amplpy (no
  `--skip-pip`), in the same cell or an earlier one. Importing amplpy puts the module
  directories first on `PATH`; the `--bin-dir` directories are put first again then.
- **Timeouts.**
  - A notebook stops at its first error. CI (nbval) runs the remaining cells too and
    reports each cell that fails.
  - A notebook's own solver time limits (`lim:time=`, `timelim=`, `timelimit=`,
    `TimeLimit=`, `time_limit =`, `maxtime=`, in its code cells, outside lines that are
    comments) raise the timeouts. For each cell that sets one, the largest limit × 1.3 +
    60 s is computed (a cell is taken to run one solve). The
    cell timeout becomes the largest of these values, and the notebook timeout their sum,
    at least twice the cell timeout. A cell that solves several times in a loop can still
    need a larger `--cell-timeout` or `--nb-timeout`.
- **Watchdog.** It stops a notebook when either limit is exceeded:
  - the notebook timeout;
  - `--mem-gb`, for the resident memory of the notebook's processes.

  When free memory falls below `--reserve-gb`, it stops the largest running notebook.
  Afterwards it kills the processes that the notebook left running (with `psutil`): a
  stopped kernel leaves its AMPL and solver processes behind.
- **Statuses.** Each notebook gets one of these statuses:
  - `ok`;
  - `error` (an exception, shown with the cell number; `prelude` for the cell that the
    script adds);
  - `cell_timeout` (shown with the cell number), `nb_timeout`;
  - `memory_limit`, `memory_guard`;
  - `no_output` (the worker wrote no notebook: see the `.log` file next to the executed
    notebook);
  - `runner_error` (the script or the kernel failed for this notebook, for example a
    kernel that died; the exception and the cell are shown).

### Reading the comparison

The comparison takes the solver headlines, such as `HiGHS 1.15.1: optimal solution;
objective 85`. It matches them cell by cell with the outputs stored in the notebook and
reports changed statuses, objective values differing by more than 1e-5 relative (by more
than 1e-5 absolute for values below 1 in magnitude, so that solver round-off near zero is
not reported; `--rel-tol` changes this), and changed numbers of solves. `summary.md` also
lists warnings that are new compared with the stored outputs. Treat a difference as a lead, not a verdict:

- Stored outputs are often from older AMPL and solver versions. A time-limited run, or a
  newer solver, finds other incumbents or proves optimality.
- Notebooks with random data and no seed are marked `(random data without seed)` in
  `summary.md` (a guess from the code: `random`, `randint`, `np.random`, ... and no `seed`).
  Notebooks that download data may compare against different data. Those that used
  synthetic data are marked `(synthetic data)`: their objective values differ from the
  stored ones.
- Only cells that have stored outputs are compared, and after an error or a timeout only
  the cells up to the failed one. Cells whose outputs show no solver headline count as zero
  solves.
- To tell a solver version from an AMPL or driver change, run the notebook twice: once with
  the released modules and once with `--bin-dir`. Then compare the two `summary.md` files.

### Downloaded data

Notebooks that download stock prices from Yahoo Finance (`yfinance`) have a Data section
with `download_close()`. It uses synthetic prices, correlated random walks with a fixed
seed, when `USE_SYNTHETIC_DATA = True` is set in the notebook or the environment variable
`COLAB_SYNTHETIC_DATA` is `1` (or `true`, `yes`), and also when the download fails or misses
a ticker. The notebook then prints `Using synthetic data: ...`, which the script detects.
Downloads from CI runners fail now and then, and Yahoo's data is for personal use, so it is
not kept in the repository.

CI does not report this fallback: a notebook passes with synthetic data too, so a lasting
download problem shows only in the job log or in a run of this script.

The five copies of the Data section are the same apart from their imports;
`authors/mukeshwaran/Notebook_4_Porfolio_Optimization_Risk_Strategies.ipynb` is the one to
copy. Give a new notebook that downloads data the same fallback, and check that its models
stay feasible with synthetic data (`--synthetic-data`). A change to the section goes into
all copies.

### Tests of the script

`scripts/tests/test_run_notebooks.py` runs the script on small notebooks that the tests
write into a temporary copy of the repository: timeouts, statuses and error cells, the
`--bin-dir` replacement of `ampl_notebook()` and the order of `PATH`, folder copies, list
files, `--out`, `--recompare`, interruption and `--synthetic-data`; other tests call the
comparison and the timeout functions directly. The notebooks print solver headlines
instead of solving, and the `--bin-dir` tests use a stub amplpy package, so no AMPL,
solver, license or amplpy is needed. They need pytest, nbclient, nbformat and ipykernel,
and psutil for the interruption test (skipped on Windows); they take about 20 seconds. CI
runs them on every push:

```bash
python -m pytest scripts/tests
```

### Notes

- **AMPL license.** AMPL looks for `ampl.lic` along `PATH`, and importing amplpy puts the
  module directories first. Without `--licfile`, an AMPL given by `--bin-dir` may therefore
  run with the license of the `base` module, which can be a size-limited demo license.
- **Certificates.** Python from python.org on macOS has no CA certificates. The script sets
  `SSL_CERT_FILE` from `certifi` when it is installed, for notebooks that download data.
- **Table handlers.** With `--bin-dir`, the table handlers of the `plugins` module (amplxl,
  amplcsv, ...) are added to `ampl_libpath`, if that module is installed.
- **Results.** The results folder `notebook-runs/` is ignored by git, ruff,
  `check_headers.py` and `list_notebooks.py`.
- **Saving outputs.** The script never changes the notebooks. To save new outputs in a
  notebook, run it with the released modules and copy the outputs over, keeping the outputs
  of the first two cells as they are (the integration cell prints the license in use). Then
  check them for local paths, local license lines and messages of development builds before
  committing.
