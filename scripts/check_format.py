"""Check that the notebooks and scripts are formatted and lint-clean according
to ruff (configured in ruff.toml), without modifying any files.

This is what the CI lint job runs. Run from anywhere with:

    $ python scripts/check_format.py

To apply the fixes, use scripts/format_code.py.
"""

import os
import subprocess
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    returncode = 0
    for args in (["format", "--check", "--diff", "."], ["check", "."]):
        result = subprocess.run(
            [sys.executable, "-m", "ruff", *args], cwd=ROOT_DIR, check=False
        )
        returncode = returncode or result.returncode
    sys.exit(returncode)


if __name__ == "__main__":
    main()
