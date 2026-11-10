"""Lint-fix and format the notebooks and scripts with ruff (configured in
ruff.toml).

Runs `ruff check --fix` (safe lint fixes) followed by `ruff format` from the
repository root. Run from anywhere with:

    $ python scripts/format_code.py

To check without modifying any files (as in CI), use scripts/check_format.py.
"""

import os
import subprocess
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    returncode = 0
    for args in (["check", "--fix", "."], ["format", "."]):
        result = subprocess.run(
            [sys.executable, "-m", "ruff", *args], cwd=ROOT_DIR, check=False
        )
        returncode = returncode or result.returncode
    sys.exit(returncode)


if __name__ == "__main__":
    main()
