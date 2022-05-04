import json
from utils import list_notebooks, list_badges
import os

os.chdir(os.path.dirname(__file__) or os.curdir)
os.chdir("..")

NOTEBOOKS = list_notebooks()

for info in NOTEBOOKS:
    title, fname = info["title"], info["fname"]
    print(f"Updating {fname}: {title}")
    data = json.load(open(fname, "r"))
    cells = data["cells"]
    assert cells[0]["cell_type"] == "markdown"
    header = cells[0]["source"]
    assert header[0].startswith("#")

    # Remove old badges
    header = [row for row in header if not row.startswith("[![")]

    # Update badges
    colab_only = info["colab_only"]
    badges = list_badges(fname, colab_only)
    if header[1] != "\n":
        header.insert(1, "\n")
    header.insert(1, " ".join(badges) + "\n")

    # Remove empty lines
    remove = []
    for i, row in enumerate(header):
        if row == "\n" and header[i - 1] == "\n":
            remove.append(i)
    for i in reversed(remove):
        print(f"removing newline in line {i}")
        del header[i]

    # Update header with new badges
    cells[0]["source"] = header

    open(fname, "w").write(
        json.dumps(data, separators=(",", ":"), ensure_ascii=False) + "\n"
    )
