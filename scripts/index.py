from utils import list_notebooks, list_badges
import glob
import os

os.chdir(os.path.dirname(__file__) or os.curdir)
os.chdir("..")

NOTEBOOKS = list_notebooks()


readme = open("README.md", "w")
index = open("docs/source/index.rst", "w")

print(
    """# AMPL Model Colaboratory

## Website

https://colab.ampl.com

## Contribution Guide

1. Use the template [template/colab.ipynb](https://github.com/ampl/amplcolab/blob/master/template/colab.ipynb) as base template.

2. In the header make sure you fill the following fields:
```
Description: <required>

Tags: <required>, <>, <>

Notebook author: <required>

Model author: <required>

License: <optional>

References: <optional>
```

3. Do not modify the initial cells that take care of setup and jupyter notebook integration.

4. Update the badges and the index as shown below before committing.

Note: The default license for every notebook is [MIT](https://github.com/ampl/amplcolab/blob/master/LICENSE) unless specified otherwise in the notebook.

### Updating badges & headers

The following command will patch every notebook in the repository with badges corresponding to the notebook location:
```bash
$ python scripts/headers.py
```

### Updating index

The following command updates the readme file and the index in the documentation:
```bash
$ python scripts/index.py
```

## Notebooks

| Title  | GitHub |  Colab | Kaggle | Gradient | SageMaker|
|--------|--------|--------|--------|----------|----------|""",
    file=readme,
)

print(
    """
AMPL Model Colaboratory
=======================

Introduction
------------

AMPL Model Colaboratory is a collection of AMPL models in Jupyter Notebooks
that run on platforms such as Google Colab, Kaggle, Gradient, and AWS SageMaker.

In order to be use AMPL on these platforms you just need to following two code blocks
at the beginning of your notebook:

.. code-block:: bash

   # Install dependencies
   !pip install -q amplpy



.. code-block:: python

   # Google Colab & Kaggle interagration
   MODULES=['ampl', 'coin', 'highs']
   from amplpy import tools
   ampl = tools.ampl_notebook(modules=MODULES, globals_=globals()) # instantiate AMPL object and register magics


In the list ``MODULES`` you can specify the AMPL solvers you want to use in your notebook.
As a quick-start you can use our template notebook: :ref:`tag-template`.
You can contribute to this repository by making pull requests to https://github.com/ampl/amplcolab and following the instructions in the  `README.md <https://github.com/ampl/amplcolab/blob/master/README.md>`_ file.

Index
-----

.. toctree::
    :maxdepth: 1

    tags/ampl-lecture
    tags/finance
    tags/industry
    tags/military
    tags/google-sheets
    tags/index
    authors/index

Notebooks
---------

""",
    file=index,
)


def print_markdown(info, fout):
    fname = info["fname"]
    colab_only = info["colab_only"]
    badges = list_badges(fname, colab_only)
    print(f"|{info['title']}|{'|'.join(badges)}|", file=fout)


def print_rst(info, fout):
    fname, title = info["fname"], info["title"]
    colab_only = info["colab_only"]
    badges = list_badges(fname, colab_only, rst=True)
    print(title + "\n" + "^" * len(title), file=fout)
    description = info.get("description", None)
    if description:
        print(f"Description: {description}\n", file=fout)
    tags = info.get("tags", None)
    if tags:
        print(f'Tags: {", ".join(tags)}\n', file=fout)
    author = info.get("notebook_author", None)
    if author:
        print(f"Author: {author}\n", file=fout)
    print("\n".join(badges) + "\n", file=fout)


madeby = {}
tagged = {}
for info in NOTEBOOKS:
    title, fname = info["title"], info["fname"]
    for tag in info.get("tags", []):
        if tag not in tagged:
            tagged[tag] = []
        tagged[tag].append(info)
    for author in info.get("notebook_author", "").split(","):
        author = author.strip()
        if "<" not in author:
            continue
        email = author[author.find("<") + 1 : author.rfind(">")].strip()
        name = author[: author.find("<")].strip()
        if email not in madeby:
            madeby[email] = []
        madeby[email].append((name, info))

    print_markdown(info, readme)
    print_rst(info, index)

print(
    """## License

MIT

***
Copyright © 2022-2022 AMPL Optimization inc. All rights reserved.
""",
    file=readme,
)

# Tags

for f in glob.glob("docs/source/tags/*.rst"):
    os.remove(f)
tags_index = """
Tags
====

.. toctree::
    :maxdepth: 1

"""
for tag in sorted(tagged):
    tags_index += f"    {tag}\n"
print(tags_index, file=open(f"docs/source/tags/index.rst", "w"))

for tag in tagged:
    tag_rst = open(f"docs/source/tags/{tag}.rst", "w")
    title = f"{tag}"
    title += "\n" + "=" * len(title) + "\n"
    header = f".. _tag-{tag}:\n\n{title}"
    print(header, file=tag_rst)
    for info in tagged[tag]:
        print_rst(info, tag_rst)

# Authors

for f in glob.glob("docs/source/authors/*.rst"):
    os.remove(f)
authors_index = """
Authors
=======

.. toctree::
    :maxdepth: 1

"""
for email in madeby:
    email = email.lower().replace("@", "_at_")
    authors_index += f"    {email}\n"
print(authors_index, file=open(f"docs/source/authors/index.rst", "w"))

for email, infolst in madeby.items():
    email = email.replace("@", "_at_")
    email_rst = open(f"docs/source/authors/{email}.rst", "w")
    title = f"{infolst[0][0]}"
    title += "\n" + "=" * len(title) + "\n"
    header = f".. _email-{email}:\n\n{title}"
    print(header, file=email_rst)
    for _, info in infolst:
        print_rst(info, email_rst)
