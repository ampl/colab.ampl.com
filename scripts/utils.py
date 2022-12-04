import os
import re
import json


def read_header(fname):
    notebook = open(fname, "r", encoding='utf-8').read()
    data = json.loads(notebook)
    cells = data["cells"]
    assert cells[0]["cell_type"] == "markdown"
    header = cells[0]["source"]
    assert header[0].startswith("#")
    info = {
        "fname": fname,
        "title": header[0].lstrip("# ").rstrip("\n"),
        "colab_only": " gspread" in notebook,
    }
    for row in header:
        if ":" not in row:
            continue
        row = row.strip()
        key = row[: row.find(":")].strip().lower().replace(" ", "_")
        value = row[row.find(":") + 1 :].strip()
        if key in ("description", "notebook_author", "model_author"):
            assert key not in info
            info[key] = value
        elif key == "tags":
            assert key not in info
            info[key] = [t.strip().lower() for t in value.split(",")]
    return info


def list_notebooks():
    lst = [
        os.path.join(dirpath, fname)[2:].replace(os.path.sep, '/')
        for (dirpath, _, files) in os.walk(".")
        for fname in files
        if fname.endswith(".ipynb") and ".ipynb_checkpoints" not in dirpath
    ]
    lst = [fname for fname in lst if "site-packages" not in fname]

    notebooks = []
    for fname in lst:
        print(f"Processing: {fname}")
        info = read_header(fname)
        title = info["title"]
        notebooks.append(info)
        print(f"Title: {title}\n")
    notebooks.sort(key=lambda info: info["title"])
    return notebooks


GITHUB_PATH = "ampl/amplcolab/blob/master/"


def normalize(url):
    return re.sub(r"([^:])//+", r"\1/", url)


def github_badge(fname, rst=False):
    basename = os.path.basename(fname)
    image = "https://img.shields.io/badge/github-%23121011.svg?logo=github"
    url = normalize(f"https://github.com/{GITHUB_PATH}/{fname}")
    if not rst:
        return f"[![{basename}]({image})]({url})"
    return f""".. image:: {image}
    :target: {url}
    :alt: {basename}
    """


def colab_badge(fname, rst=False):
    prefix = "https://colab.research.google.com/github"
    image = "https://colab.research.google.com/assets/colab-badge.svg"
    url = normalize(f"{prefix}/{GITHUB_PATH}/{fname}")
    if not rst:
        return f"[![Open In Colab]({image})]({url})"
    return f""".. image:: {image}
    :target: {url}
    :alt: Open In Colab
    """


def kaggle_badge(fname, rst=False):
    prefix = "https://kaggle.com/kernels/welcome?src=https://github.com"
    image = "https://kaggle.com/static/images/open-in-kaggle.svg"
    url = normalize(f"{prefix}/{GITHUB_PATH}/{fname}")
    if not rst:
        return f"[![Kaggle]({image})]({url})"
    return f""".. image:: {image}
    :target: {url}
    :alt: Kaggle
    """


def gradient_badge(fname, rst=False):
    prefix = "https://console.paperspace.com/github"
    image = "https://assets.paperspace.io/img/gradient-badge.svg"
    url = normalize(f"{prefix}/{GITHUB_PATH}/{fname}")
    if not rst:
        return f"[![Gradient]({image})]({url})"
    return f""".. image:: {image}
    :target: {url}
    :alt: Gradient
    """


def sagemaker_badge(fname, rst=False):
    prefix = "https://studiolab.sagemaker.aws/import/github"
    image = "https://studiolab.sagemaker.aws/studiolab.svg"
    url = normalize(f"{prefix}/{GITHUB_PATH}/{fname}")
    if not rst:
        return f"[![Open In SageMaker Studio Lab]({image})]({url})"
    return f""".. image:: {image}
    :target: {url}
    :alt: Open In SageMaker Studio Lab
    """


def list_badges(fname, colab_only=False, rst=False):
    github = github_badge(fname, rst=rst)
    colab = colab_badge(fname, rst=rst)
    kaggle = kaggle_badge(fname, rst=rst) if not colab_only else ""
    gradient = gradient_badge(fname, rst=rst) if not colab_only else ""
    sagemaker = sagemaker_badge(fname, rst=rst) if not colab_only else ""
    return [
        badge for badge in (github, colab, kaggle, gradient, sagemaker) if badge != ""
    ]
