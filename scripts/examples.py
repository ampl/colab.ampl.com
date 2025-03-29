from utils import list_badges
import json
import re
import os


AMPL_BOOK_SRC_DIR = "ampl-book-src"
AMPL_BOOK_DST_DIR = "../ampl-book"
AMPL_LECTURE_SRC_DIR = "ampl-lecture-src"
AMPL_LECTURE_DST_DIR = "../ampl-lecture"


def notebook_headers(
    fname,
    title,
    description,
    tags=[],
    author="N/A",
    model_author="N/A",
    dependencies=[],
    modules=["ampl", "coin"],
):
    badges = list_badges(fname.replace("../", ""), colab_only=False)
    modules_str = ", ".join(["'" + m + "'" for m in modules])
    return [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                f"# {title}\n",
                f"{' '.join(badges)}\n",
                "\n",
                f"Description: {description}\n",
                "\n",
                f"Tags: {', '.join(tags)}\n",
                "\n",
                f"Notebook author: {author}\n",
                "\n",
                f"Model author: {model_author}\n",
            ],
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Install dependencies\n",
                "%pip install -q amplpy==0.15.0b2" + " ".join(dependencies),
            ],
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Google Colab & Kaggle integration\n",
                "from amplpy import AMPL, ampl_notebook\n",
                "\n",
                "ampl = ampl_notebook(\n",
                f"    modules={modules_str},  # modules to install\n",
                '    license_uuid="default",  # license to use\n',
                ")  # instantiate AMPL object and register magics",
            ],
        },
    ]


def markdown_cell(content):
    lines = [line + "\n" for line in content.split("\n")]
    if lines != []:
        lines[-1] = lines[-1].rstrip("\n")
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": lines,
    }


def code_cell(content):
    lines = [line + "\n" for line in content.split("\n")]
    if lines != []:
        lines[-1] = lines[-1].rstrip("\n")
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": lines,
    }


def generate_notebook(fname, cells):
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3 (ipykernel)",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.9.8",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 2,
    }
    open(fname, "w", newline="\n", encoding="utf-8").write(
        json.dumps(notebook, separators=(",", ": "), indent="  ", ensure_ascii=False)
    )


def book_example(name, title, description, tags, markdown_header, files, ampl_commands):
    from os import path

    notebook_fname = f"{AMPL_BOOK_DST_DIR}/{name}.ipynb"
    modules = ["ampl", "coin"]
    solvers = re.findall(r"option\s+solver\s+([^\s;]+)\s*;", ampl_commands)
    for solver in solvers:
        if solver not in ("cbc", "ipopt", "bonmin", "couenne"):
            modules.append(solver)
    if len(modules) > 2:
        print("Using modules:", modules)
    else:
        print("Using default modules:", modules)
    cells = notebook_headers(
        notebook_fname, title=title, description=description, tags=tags, modules=modules
    )
    cells.append(markdown_cell(markdown_header))
    for fname in files:
        code = (
            f"%%writefile {path.basename(fname)}\n"
            + open(fname, "r", encoding="utf-8").read()
        )
        cells.append(code_cell(code))
    cells.append(code_cell("%%ampl_eval\n" + ampl_commands))
    generate_notebook(notebook_fname, cells)
    print(f"Generated {notebook_fname}.")


def ampl_lecture(name, title, description, tags, markdown):
    notebook_fname = f"{AMPL_LECTURE_DST_DIR}/{name}.ipynb"
    modules = ["ampl", "coin"]
    solvers = re.findall(r"option\s+solver\s+([^\s;]+)\s*;", markdown)
    for solver in solvers:
        if solver not in ("cbc", "ipopt", "bonmin", "couenne"):
            modules.append(solver)
    if len(modules) > 2:
        print("Using modules:", modules)
    else:
        print("Using default modules:", modules)
    cells = notebook_headers(
        notebook_fname, title=title, description=description, tags=tags, modules=modules
    )

    rgx = re.compile(r"```cell[^`]+```")
    marker = "!code-cell!"
    code_cells = re.findall(rgx, markdown)
    markdown = re.sub(rgx, marker, markdown)
    assert len(code_cells) == markdown.count(marker)
    while markdown != "":
        p = markdown.find(marker)
        if p == -1:
            md = markdown.strip()
            if md != "":
                cells.append(markdown_cell(md))
            break
        md = markdown[:p].strip()
        if md != "":
            cells.append(markdown_cell(md))
        code = code_cells.pop(0)
        code = code.replace("```cell", "").strip("\r\n `")
        cells.append(code_cell(code))
        markdown = markdown[p + len(marker) :]
    assert code_cells == []

    generate_notebook(notebook_fname, cells)
    print(f"Generated {notebook_fname}.")


def config_book_example(
    fname,
    mod_fname=None,
    dat_fname=None,
    run_fname=None,
    md_fname=None,
    description=None,
):
    if not mod_fname:
        mod_fname = f"{fname}.mod"
    if not dat_fname:
        dat_fname = f"{fname}.dat"
    if not run_fname:
        run_fname = f"{fname}.run"
    if not description:
        description = f"book example autogenerated using {mod_fname}, {dat_fname}, and {run_fname}"
    if md_fname:
        markdown_header = open(
            f"{AMPL_BOOK_SRC_DIR}/{md_fname}", "r", encoding="utf-8"
        ).read()
    else:
        markdown_header = f"### Example: {fname}\n"
        markdown_header += (
            f"autogenerated using {mod_fname}, {dat_fname}, and {run_fname}"
        )
        # open(f"{AMPL_BOOK_SRC_DIR}/{fname}.md", "w", newlines="\n") .write(markdown_header)
    return {
        "name": fname,
        "title": f"Book Example: {fname}",
        "description": description,
        "tags": ["ampl-only", "ampl-book"],
        "markdown_header": markdown_header,
        "files": [
            f"{AMPL_BOOK_SRC_DIR}/{mod_fname}",
            f"{AMPL_BOOK_SRC_DIR}/{dat_fname}",
        ],
        "ampl_commands": open(
            f"{AMPL_BOOK_SRC_DIR}/{run_fname}", "r", encoding="utf-8"
        ).read(),
    }


def config_ampl_lecture(fname, md_fname, title=None, description=None):
    return {
        "name": fname,
        "markdown": open(
            f"{AMPL_LECTURE_SRC_DIR}/{md_fname}", "r", encoding="utf-8"
        ).read(),
        "title": title,
        "description": description,
        "tags": ["ampl-only", "ampl-lecture"],
    }


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__) or os.curdir)
    BOOK_EXAMPLES = [
        config_book_example(
            fname, mod_fname, dat_fname, run_fname, md_fname, description
        )
        for fname, mod_fname, dat_fname, run_fname, md_fname, description in [
            ("diet", "diet.mod", "diet.dat", "diet.run", "diet.md", None),
            ("econ", "econ.mod", "econ.dat", "econ.run", "econ.md", None),
            (
                "multmip1",
                "multmip1.mod",
                "multmip1.dat",
                "multmip1.run",
                "multmip1.md",
                None,
            ),
            ("net1", "net1.mod", "net1.dat", "net1.run", "net1.md", None),
            (
                "nltrans",
                "nltransd.mod",
                "nltrans.dat",
                "nltrans.run",
                "nltrans.md",
                None,
            ),
            ("prod", "prod.mod", "prod.dat", "prod.run", "prod.md", None),
            ("steel", "steel.mod", "steel.dat", "steel.run", "steel.md", None),
            ("transp", "transp.mod", "transp.dat", "transp.run", "transp.md", None),
        ]
    ]

    for example in BOOK_EXAMPLES:
        book_example(
            name=example["name"],
            title=example["title"],
            description=example["description"],
            tags=example["tags"],
            markdown_header=example["markdown_header"],
            files=example["files"],
            ampl_commands=example["ampl_commands"],
        )

    AMPL_LECTURES = [
        config_ampl_lecture(fname, md_fname, title, description)
        for fname, md_fname, title, description in [
            (
                "diet_case_study",
                "diet_case_study.md",
                "Diet lecture",
                "Diet case study",
            ),
            (
                "prod_lecture",
                "prod_lecture.md",
                "Production model",
                "generic model for production problem",
            ),
            (
                "transp_lecture",
                "transp_lecture.md",
                "Transportation problem",
                "an AMPL model for the transportation problem",
            ),
            (
                "steel_lecture",
                "steel_lecture.md",
                "Steel industry problem",
                "model for steel production problem",
            ),
        ]
    ]

    for lecture in AMPL_LECTURES:
        ampl_lecture(
            name=lecture["name"],
            title=lecture["title"],
            description=lecture["description"],
            tags=lecture["tags"],
            markdown=lecture["markdown"],
        )
