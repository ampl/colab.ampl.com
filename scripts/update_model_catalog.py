"""Download the model catalog spreadsheet into docs/model-catalog.csv.

The catalog adds domain, model type, adoption level, and algorithm metadata to
the notebooks (matched through the "Model Link" column). The docs build reads
the committed CSV, so re-run this script and commit the result to refresh it:

    $ python scripts/update_model_catalog.py
    $ git add docs/model-catalog.csv
"""

import csv
import io
import os
import sys
import urllib.request

import utils

SHEET_ID = "1rfAHkpc7D0ToV-eC_f5rQxQkKlq7uK5aNRjVBsS9jUU"
SHEET_GID = "822295668"
EXPORT_URL = (
    f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export"
    f"?format=csv&gid={SHEET_GID}"
)
REQUIRED_COLUMNS = ["domain", "model_type", "adoption_level", "model_link"]


def main():
    repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    with urllib.request.urlopen(EXPORT_URL) as response:
        text = response.read().decode("utf-8")
    rows = list(csv.reader(io.StringIO(text)))
    columns = [utils.catalog_column(name) for name in rows[0]]
    missing = [col for col in REQUIRED_COLUMNS if col not in columns]
    if missing:
        sys.exit(f"Unexpected spreadsheet layout, missing columns: {missing}")

    fname = os.path.join(repo_dir, utils.MODEL_CATALOG)
    with open(fname, "w", encoding="utf-8", newline="") as f:
        csv.writer(f, lineterminator="\n").writerows(rows)

    catalog = utils.load_model_catalog(fname)
    notebooks = {info["url_string"] for info in utils.discover_notebooks(repo_dir)}
    unknown = sorted(set(catalog) - notebooks)
    print(f"Wrote {len(rows) - 1} rows ({len(catalog)} models) to {fname}")
    print(f"Notebooks without a catalog entry: {len(notebooks - set(catalog))}")
    for slug in unknown:
        print(f"Warning: catalog links to unknown notebook '{slug}'")


if __name__ == "__main__":
    main()
