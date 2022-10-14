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

    for i in range(1, len(cells)):
        assert len(cells[i]["source"]) > 0
        if cells[i]["source"][0].startswith("# Google Colab & Kaggle interagration"):
            assert cells[i]["cell_type"] == "code"
            modules = cells[i]["source"][1]
            assert modules.startswith("MODULES")
            cells[i]["source"] = [
                "# Google Colab & Kaggle interagration\n",
                modules,
                "from amplpy import tools\n",
                "ampl = tools.ampl_notebook(modules=MODULES, globals_=globals()) # instantiate AMPL object and register magics",
            ]
            break

    open(fname, "w").write(
        json.dumps(data, separators=(",", ":"), ensure_ascii=False) + "\n"
    )
