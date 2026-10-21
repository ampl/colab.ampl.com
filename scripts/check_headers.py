"""Check the notebook header fields used by the notebook search and filters.

Every notebook needs Domain, Model type and Level, with values from
docs/finder-values.json, in the hidden block after "Tags:":

    <!--
    Domain: Energy
    Subdomain: Hydrogen Production
    Model type: MILP
    Level: Case Study
    Algorithm: Rolling Horizon
    Subject: Hydrogen Facility Operations
    -->

Subdomain, Algorithm and Subject are optional (free text); leave them out
rather than empty. Run from the repository root:

    $ python scripts/check_headers.py
"""

import contextlib
import io
import json
import os
import sys

import utils

VALUES_FILE = "docs/finder-values.json"
LABELS = {
    "domain": "Domain",
    "subdomain": "Subdomain",
    "model_type": "Model type",
    "level": "Level",
    "algorithm": "Algorithm",
    "subject": "Subject",
}
REQUIRED = ["domain", "model_type", "level"]


def header_lines(fname):
    """The header cell's lines, and whether each is inside <!-- -->."""
    with open(fname, encoding="utf-8") as f:
        source = json.load(f)["cells"][0]["source"]
    inside = False
    for row in source:
        row = row.strip()
        if row.startswith("<!--"):
            inside = True
        yield row, inside
        if row.endswith("-->"):
            inside = False


def check_notebook(fname, base_dir, allowed):
    labels = [label for row, _ in header_lines(fname) for label in LABELS.values()
              if row.startswith(label + ":")]
    repeated = sorted({label for label in labels if labels.count(label) > 1})
    if repeated:
        return [f'"{label}:" appears more than once' for label in repeated]
    try:
        info = utils.read_header(base_dir, fname)
    except Exception as e:
        return [f"cannot read the header ({type(e).__name__}: {e})"]
    problems = []
    for key in REQUIRED:
        if not info.get(key):
            problems.append(f'missing "{LABELS[key]}:"')
    for key, label in LABELS.items():
        if key in info and not info[key]:
            problems.append(f'"{label}:" is empty (leave it out instead)')
    for key, values in allowed.items():
        for value in info.get(key, []):
            if value not in values:
                problems.append(
                    f'{LABELS[key]} "{value}" is not allowed; use one of: '
                    f'{", ".join(values)} (or add it to {VALUES_FILE})'
                )
    keys = tuple(label + ":" for label in LABELS.values())
    for row, inside in header_lines(fname):
        if row.startswith(keys) and not inside:
            problems.append(f'"{row}" is outside the <!-- --> block, so it is displayed')
    return problems


def main():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    with open(os.path.join(base_dir, VALUES_FILE), encoding="utf-8") as f:
        values = json.load(f)
    allowed = {key: list(values[key]) for key in REQUIRED}
    with contextlib.redirect_stdout(io.StringIO()):
        fnames = utils.notebook_files(base_dir)

    failed = 0
    for fname in fnames:
        problems = check_notebook(fname, base_dir, allowed)
        if problems:
            failed += 1
            print(os.path.relpath(fname, base_dir).replace("\\", "/"))
            for problem in problems:
                print(f"  - {problem}")
    if failed:
        sys.exit(f"\n{failed} of {len(fnames)} notebooks have header problems.")
    print(f"All {len(fnames)} notebook headers are OK.")


if __name__ == "__main__":
    main()
