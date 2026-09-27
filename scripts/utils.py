import os
import re
import csv
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
        if ".virtual_documents" not in dirpath
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


def deepnote_badge(fname, rst=False, rst_sub=""):
    if rst_sub:
        rst_sub = f"|{rst_sub}| "
    prefix = "https://deepnote.com/launch?url=https://github.com"
    image = "https://deepnote.com/buttons/launch-in-deepnote-small.svg"
    url = normalize(f"{prefix}/{GITHUB_PATH}/{fname}")
    if not rst:
        return f"[![Open In Deepnote]({image})]({url})"
    return f""".. {rst_sub}image:: {image}
    :target: {url}
    :alt: Open In Deepnote
    """


def kaggle_badge(fname, rst=False, rst_sub=""):
    if rst_sub:
        rst_sub = f"|{rst_sub}| "
    prefix = "https://kaggle.com/kernels/welcome?src=https://github.com"
    image = "https://kaggle.com/static/images/open-in-kaggle.svg"
    url = normalize(f"{prefix}/{GITHUB_PATH}/{fname}")
    if not rst:
        return f"[![Open In Kaggle]({image})]({url})"
    return f""".. {rst_sub}image:: {image}
    :target: {url}
    :alt: Open In Kaggle
    """


def gradient_badge(fname, rst=False, rst_sub=""):
    if rst_sub:
        rst_sub = f"|{rst_sub}| "
    prefix = "https://console.paperspace.com/github"
    image = "https://assets.paperspace.io/img/gradient-badge.svg"
    url = normalize(f"{prefix}/{GITHUB_PATH}/{fname}")
    if not rst:
        return f"[![Open In Gradient]({image})]({url})"
    return f""".. {rst_sub}image:: {image}
    :target: {url}
    :alt: Open In Gradient
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
        return f"[![Powered by AMPL]({badge})](https://ampl.com)"
    return ""


def list_badges(fname, colab_only=False, rst=False, page=None):
    github = github_badge(fname, rst=rst)
    colab = colab_badge(fname, rst=rst)
    deepnote = deepnote_badge(fname, rst=rst)
    kaggle = kaggle_badge(fname, rst=rst) if not colab_only else ""
    gradient = gradient_badge(fname, rst=rst) if not colab_only else ""
    sagemaker = sagemaker_badge(fname, rst=rst) if not colab_only else ""
    hits = hits_badge(fname, rst=rst) if page != "README" else ""
    return [
        badge
        for badge in (github, colab, deepnote, kaggle, gradient, sagemaker, hits)
        if badge != ""
    ]


def rst_badges(fname, url_string, colab_only=False):
    github = github_badge(fname, rst=True, rst_sub=f"github-{url_string}")
    colab = colab_badge(fname, rst=True, rst_sub=f"colab-{url_string}")
    lst = [("github", github), ("colab", colab)]
    if not colab_only:
        deepnote = deepnote_badge(fname, rst=True, rst_sub=f"deepnote-{url_string}")
        kaggle = kaggle_badge(fname, rst=True, rst_sub=f"kaggle-{url_string}")
        gradient = gradient_badge(fname, rst=True, rst_sub=f"gradient-{url_string}")
        sagemaker = sagemaker_badge(fname, rst=True, rst_sub=f"sagemaker-{url_string}")
        lst += [
            ("deepnote", deepnote),
            ("kaggle", kaggle),
            ("gradient", gradient),
            ("sagemaker", sagemaker),
        ]

    badges = " ".join((f"|{badge[0]}-{url_string}|" for badge in lst))
    images = "\n" + "\n".join((badge[1] for badge in lst)) + "\n"
    return badges, images


def print_rst(info, fout, notebooks_path=None, toc_tree=False):
    fname, title, url_string = info["fname"], info["title"], info["url_string"]
    colab_only = info["colab_only"]
    print(title + "\n" + "^" * len(title), file=fout)
    description = info.get("description", None)
    if notebooks_path:
        print(
            f"| `Notebooks <{notebooks_path}index.html>`_ > `{title} <{notebooks_path}{url_string}.html>`_",
            file=fout,
        )
    badges, images = rst_badges(fname, url_string, colab_only=colab_only)
    print(f"| {badges}", file=fout)
    if description:
        print(f"| Description: {description}", file=fout)

    tags = info.get("tags", None)
    if tags:
        tags = [f":ref:`tag-{tag}`" for tag in tags]
        print(f'| Tags: {", ".join(tags)}', file=fout)
    authors = info.get("notebook_author", None)
    if authors:
        authors = authors.replace("<<", "<").replace(">>", ">")
        lst = []
        for author in authors.split(","):
            author = author.strip()
            if "<" in author:
                name = author[: author.find("<")]
                email = author[author.find("<") + 1 : author.find(">")]
                lst.append(f":ref:`email-{email.replace('@', '_at_')}` <{email}>")
            else:
                lst.append(author)
        print(f"| Author: {', '.join(lst)}", file=fout)
    if toc_tree:
        print(
            f"""
        .. toctree::
            :maxdepth: 2
            :caption: {title}
            :glob:

            {notebooks_path}{url_string}.ipynb
        """,
            file=fout,
        )
    print(images, file=fout)
    print(file=fout)


def parse_authors(notebook_author):
    """Split 'Name <<email>>, Name <<email>>' into a list of names."""
    names = []
    for author in (notebook_author or "").split(","):
        name = author.split("<")[0].strip()
        if name and name.upper() != "N/A":
            names.append(name)
    return names


def parse_author_pages(notebook_author):
    """Author page names ('gleb_at_ampl.com') for 'Name <<email>>, ...'."""
    return [
        email.strip().lower().replace("@", "_at_")
        for email in re.findall(r"<<([^<>]+)>>", notebook_author or "")
    ]


MODEL_CATALOG = "docs/model-catalog.csv"

# Catalog column -> (search index field, extra separators for multiple values)
CATALOG_FIELDS = {
    "domain": ("domains", ""),
    "subdomain": ("subdomains", ""),
    "model_type": ("model_types", "&"),
    "adoption_level": ("levels", ""),
    "advanced_algorithm": ("algorithms", ""),
    "subject": ("subjects", ""),
}
CATALOG_EMPTY = {"", "-", "n/a", "na", "none"}


def catalog_column(name):
    """'3. Model Type' -> 'model_type'"""
    name = re.sub(r"^\s*\d+\.\s*", "", name).strip().lower()
    return re.sub(r"[^a-z0-9]+", "_", name).strip("_")


def split_catalog_values(value, separators=""):
    values = []
    for part in re.split(r"[,\n" + re.escape(separators) + "]", value or ""):
        part = re.sub(r"\s+", " ", part).strip().rstrip(".")
        if part.lower() not in CATALOG_EMPTY:
            values.append(part)
    return values


def load_model_catalog(fname):
    """Read the model catalog CSV into {notebook url_string: {field: [values]}}.

    A row with a Model Link starts a model; the rows below it without a Domain
    continue that model (e.g., additional subjects).
    """
    catalog = {}
    if not os.path.exists(fname):
        return catalog
    with open(fname, encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    columns = [catalog_column(name) for name in rows[0]]
    current = None
    for row in rows[1:]:
        record = dict(zip(columns, row))
        match = re.search(r"notebooks/([^/#?]+)\.html", record.get("model_link", ""))
        if match:
            current = catalog.setdefault(match.group(1), {})
        elif record.get("domain", "").strip():
            current = None  # a model without a notebook page link
        if current is None:
            continue
        for column, (field, separators) in CATALOG_FIELDS.items():
            for value in split_catalog_values(record.get(column), separators):
                if value not in current.setdefault(field, []):
                    current[field].append(value)

    # Spell each value the same way everywhere (e.g., "Benders decomposition"
    # and "Benders Decomposition"), using its most common spelling
    for field, _ in CATALOG_FIELDS.values():
        spellings = {}
        for entry in catalog.values():
            for value in entry.get(field, []):
                spellings.setdefault(value.casefold(), []).append(value)
        canonical = {
            key: max(sorted(set(lst)), key=lst.count) for key, lst in spellings.items()
        }
        for entry in catalog.values():
            if field in entry:
                entry[field] = list(
                    dict.fromkeys(canonical[v.casefold()] for v in entry[field])
                )
    return catalog


def search_index(notebooks, catalog=None):
    """Compact per-notebook metadata used by the notebook finder."""
    catalog = catalog or {}
    index = []
    for info in notebooks:
        entry = catalog.get(info["url_string"], {})
        index.append(
            {
                "title": info["title"],
                "slug": info["url_string"],
                "description": info.get("description", ""),
                "tags": info.get("tags", []),
                "modules": [mod for mod in info.get("modules", []) if mod != "ampl"],
                "authors": parse_authors(info.get("notebook_author")),
                "author_pages": parse_author_pages(info.get("notebook_author")),
                "path": info["fname"],
                **{field: entry.get(field, []) for field, _ in CATALOG_FIELDS.values()},
            }
        )
    return index


def write_search_index(notebooks, fname, catalog=None):
    with open(fname, "w", encoding="utf-8", newline="\n") as f:
        json.dump(
            search_index(notebooks, catalog),
            f,
            ensure_ascii=False,
            separators=(",", ":"),
        )
