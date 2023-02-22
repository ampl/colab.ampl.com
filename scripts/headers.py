import json
from utils import list_notebooks, list_badges, parse_modules
import os


def update_notebook_headers():
    initial_dir = os.curdir
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
            source = cells[i]["source"]
            assert len(source) > 0
            if source[0].startswith("# Install dependencies"):
                assert cells[i]["cell_type"] == "code"
                for dependencies in source:
                    if dependencies.replace(" -q", "").startswith(
                        "!pip install amplpy"
                    ):
                        break
                else:
                    raise Exception(f"amplpy is not being installed in {fname}")
                cells[i]["outputs"] = []
                break
        else:
            raise Exception(f"Could not find dependencies cell in {fname}")

        for i in range(1, len(cells)):
            source = cells[i]["source"]
            assert len(source) > 0
            if source[0].startswith("# Google Colab & Kaggle integration"):
                assert cells[i]["cell_type"] == "code"
                src = "".join(source)
                assert "[" in src and "]" in src
                modules = list(eval(src[src.find("[") : src.find("]") + 1]))
                modules_str = "[" + ", ".join([f'"{mod}"' for mod in modules]) + "]"
                if "ampl" in modules:
                    modules.remove("ampl")
                assert len(modules) >= 1
                cells[i]["source"] = [
                    "# Google Colab & Kaggle integration\n",
                    "from amplpy import AMPL, tools\n",
                    "ampl = tools.ampl_notebook(\n",
                    f"    modules={modules_str}, # modules to install\n",
                    '    license_uuid="default", # license to use\n',
                    "    g=globals()) # instantiate AMPL object and register magics",
                ]
                # cells[i]["source"] = [
                #     "# Google Colab & Kaggle integration\n",
                #     "from amplpy import tools\n",
                #     f'MODULES, LICENSE_UUID = {modules_str}, "your-license-uuid"\n',
                #     f"ampl = tools.ampl_notebook(modules=MODULES, license_uuid=LICENSE_UUID, g=globals()) # instantiate AMPL object and register magics",
                # ]
                cells[i]["outputs"] = []
                break
        else:
            raise Exception(f"Could not find integration cell in {fname}")

        open(fname, "w", newline="\n").write(
            json.dumps(data, separators=(",", ": "), indent="  ", ensure_ascii=False)
            + "\n"
        )

    os.chdir(initial_dir)


if __name__ == "__main__":
    update_notebook_headers()
