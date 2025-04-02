import os
import re
import json


def parse_modules(cell):
    return [
        mod.strip(",'\" ")
        for mod in cell[cell.find("[") + 1 : cell.find("]")].split(",")
    ]


def url_string(title):
    title = title.lower()
    title = title.replace("&", " and ")
    title = title.strip().replace(" ", "-").replace("_", "-")
    title = re.sub(r"[^a-zA-Z0-9\-_]", "", title)
    title = re.sub(r"-+", "-", title)
    return title


def read_header(base_dir, fname):
    if not fname.startswith(base_dir):
        base_dir = abs.path.abspath(base_dir)
        fname = os.path.join(base_dir, fname)
    notebook = open(fname, "r", encoding="utf-8").read()
    data = json.loads(notebook)
    cells = data["cells"]
    assert cells[0]["cell_type"] == "markdown"
    header = cells[0]["source"]
    assert header[0].startswith("#")
    title = header[0].lstrip("# ").rstrip("\n")
    info = {
        "fname": fname[len(base_dir) + 1 :],
        "title": title,
        "abspath": os.path.abspath(fname),
        "url_string": url_string(title),
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
            info[key] = [t.strip().lower().replace(" ", "-") for t in value.split(",")]
    for i in range(1, len(cells)):
        source = cells[i]["source"]
        assert len(source) > 0
        if source[0].startswith("# Google Colab & Kaggle integration"):
            modules = parse_modules("".join(source))
            assert modules != []
            info["modules"] = modules
            break
    else:
        raise Exception("Modules not found in notebook")
    return info


def discover_notebooks(base_dir="."):
    base_dir = os.path.abspath(base_dir)
    lst = [
        os.path.join(dirpath, fname).replace("\\", "/")[len(base_dir) + 1 :]
        for (dirpath, _, files) in os.walk(base_dir)
        for fname in files
        if fname.endswith(".ipynb") and ".ipynb_checkpoints" not in dirpath
        if not dirpath[len(base_dir) + 1 :].startswith(("docs", "venv"))
    ]
    lst = [fname for fname in lst if "site-packages" not in fname]

    notebooks = []
    for fname in sorted(lst):
        fname = os.path.join(base_dir, fname)
        if "/tmp/" in fname or fname.endswith("template/minimal.ipynb"):
            print(f"Skipping {fname}.")
            continue
        print(f"Processing: {fname}")
        info = read_header(base_dir, fname)
        title = info["title"]
        notebooks.append(info)
        print(f"Title: {title}\n")
    notebooks.sort(key=lambda info: info["title"])
    return notebooks


GITHUB_PATH = "ampl/colab.ampl.com/blob/master/"


def normalize(url):
    return re.sub(r"([^:])//+", r"\1/", url)


def github_badge(fname, rst=False, rst_sub=""):
    if rst_sub:
        rst_sub = f"|{rst_sub}| "
    basename = os.path.basename(fname)
    image = "https://img.shields.io/badge/github-%23121011.svg?logo=github"
    url = normalize(f"https://github.com/{GITHUB_PATH}/{fname}")
    if not rst:
        return f"[![{basename}]({image})]({url})"
    return f""".. {rst_sub} image:: {image}
    :target: {url}
    :alt: {basename}
    """


def colab_badge(fname, rst=False, rst_sub=""):
    if rst_sub:
        rst_sub = f"|{rst_sub}| "
    prefix = "https://colab.research.google.com/github"
    image = "https://colab.research.google.com/assets/colab-badge.svg"
    url = normalize(f"{prefix}/{GITHUB_PATH}/{fname}")
    if not rst:
        return f"[![Open In Colab]({image})]({url})"
    return f""".. {rst_sub}image:: {image}
    :target: {url}
    :alt: Open In Colab
    """


def kaggle_badge(fname, rst=False, rst_sub=""):
    if rst_sub:
        rst_sub = f"|{rst_sub}| "
    prefix = "https://kaggle.com/kernels/welcome?src=https://github.com"
    image = "https://kaggle.com/static/images/open-in-kaggle.svg"
    url = normalize(f"{prefix}/{GITHUB_PATH}/{fname}")
    if not rst:
        return f"[![Kaggle]({image})]({url})"
    return f""".. {rst_sub}image:: {image}
    :target: {url}
    :alt: Kaggle
    """


def gradient_badge(fname, rst=False, rst_sub=""):
    if rst_sub:
        rst_sub = f"|{rst_sub}| "
    prefix = "https://console.paperspace.com/github"
    image = "https://assets.paperspace.io/img/gradient-badge.svg"
    url = normalize(f"{prefix}/{GITHUB_PATH}/{fname}")
    if not rst:
        return f"[![Gradient]({image})]({url})"
    return f""".. {rst_sub}image:: {image}
    :target: {url}
    :alt: Gradient
    """


def sagemaker_badge(fname, rst=False, rst_sub=""):
    if rst_sub:
        rst_sub = f"|{rst_sub}| "
    prefix = "https://studiolab.sagemaker.aws/import/github"
    image = "https://studiolab.sagemaker.aws/studiolab.svg"
    url = normalize(f"{prefix}/{GITHUB_PATH}/{fname}")
    if not rst:
        return f"[![Open In SageMaker Studio Lab]({image})]({url})"
    return f""".. {rst_sub}image:: {image}
    :target: {url}
    :alt: Open In SageMaker Studio Lab
    """


def hits_badge(fname, rst=False):
    badge = "https://h.ampl.com/" + normalize(
        f"https://github.com/{GITHUB_PATH}/{fname}"
    )
    if not rst:
        return f"[![Hits]({badge})](https://colab.ampl.com)"
    return ""


def list_badges(fname, colab_only=False, rst=False, page=None):
    github = github_badge(fname, rst=rst)
    colab = colab_badge(fname, rst=rst)
    kaggle = kaggle_badge(fname, rst=rst) if not colab_only else ""
    gradient = gradient_badge(fname, rst=rst) if not colab_only else ""
    sagemaker = sagemaker_badge(fname, rst=rst) if not colab_only else ""
    hits = hits_badge(fname, rst=rst) if page != "README" else ""
    return [
        badge
        for badge in (github, colab, kaggle, gradient, sagemaker, hits)
        if badge != ""
    ]


def rst_badges(fname, url_string, colab_only=False):
    github = github_badge(fname, rst=True, rst_sub=f"github-{url_string}")
    colab = colab_badge(fname, rst=True, rst_sub=f"colab-{url_string}")
    lst = [("github", github), ("colab", colab)]
    if not colab_only:
        kaggle = kaggle_badge(fname, rst=True, rst_sub=f"kaggle-{url_string}")
        gradient = gradient_badge(fname, rst=True, rst_sub=f"gradient-{url_string}")
        sagemaker = sagemaker_badge(fname, rst=True, rst_sub=f"sagemaker-{url_string}")
        lst += [("kaggle", kaggle), ("gradient", gradient), ("sagemaker", sagemaker)]

    badges = " ".join((f"|{badge[0]}-{url_string}|" for badge in lst))
    images = "\n" + "\n".join((badge[1] for badge in lst)) + "\n"
    return badges, images
