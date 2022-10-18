from utils import list_notebooks, list_badges
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

Tags
----

.. toctree::
    :maxdepth: 1

    tag-ampl-book
    tag-ampl-lecture
    tag-example
    tag-finance
    tag-callbacks
    tag-google-sheets
    tag-industry
    tags

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


tagged = {}
for info in NOTEBOOKS:
    title, fname = info["title"], info["fname"]
    for tag in info.get("tags", []):
        if tag not in tagged:
            tagged[tag] = []
        tagged[tag].append(info)

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

for tag in tagged:
    tag_rst = open(f"docs/source/tag-{tag}.rst", "w")
    title = f"{tag}"
    title += "\n" + "=" * len(title) + "\n"
    header = f".. _tag-{tag}:\n\n{title}"
    print(header, file=tag_rst)
    for info in tagged[tag]:
        print_rst(info, tag_rst)
