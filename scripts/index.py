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

- **Starting template**

    .. image:: https://colab.research.google.com/assets/colab-badge.svg
        :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/template/colab.ipynb
        :alt: Open In Colab
        
    .. image:: https://kaggle.com/static/images/open-in-kaggle.svg
        :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/template/colab.ipynb
        :alt: Kaggle
        
    .. image:: https://assets.paperspace.io/img/gradient-badge.svg
        :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/template/colab.ipynb
        :alt: Gradient
        
    .. image:: https://studiolab.sagemaker.aws/studiolab.svg
        :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/template/colab.ipynb
        :alt: Open In SageMaker Studio Lab

- **Christmas model written by** `ChatGPT <https://chat.openai.com/>`_

    .. image:: https://colab.research.google.com/assets/colab-badge.svg
        :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/authors/fdabrandao/miscellaneous/christmas.ipynb
        :alt: Open In Colab
        
    .. image:: https://kaggle.com/static/images/open-in-kaggle.svg
        :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/authors/fdabrandao/miscellaneous/christmas.ipynb
        :alt: Kaggle
        
    .. image:: https://assets.paperspace.io/img/gradient-badge.svg
        :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/authors/fdabrandao/miscellaneous/christmas.ipynb
        :alt: Gradient
        
    .. image:: https://studiolab.sagemaker.aws/studiolab.svg
        :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/authors/fdabrandao/miscellaneous/christmas.ipynb
        :alt: Open In SageMaker Studio Lab
        


Introduction
------------

AMPL Model Colaboratory is a collection of AMPL models in `Jupyter Notebooks <https://jupyter.org/>`_
that run on platforms such as **Google Colab**, **Kaggle**, **Gradient**, and **AWS SageMaker**.

In order to be use AMPL on these platforms you just need to following two code blocks
at the beginning of your notebook:

.. code-block:: bash

   # Install dependencies
   !pip install -q amplpy


.. code-block:: python

   # Google Colab & Kaggle integration
   MODULES = ['ampl', 'coin', 'highs', 'gokestrel']
   from amplpy import tools
   ampl = tools.ampl_notebook(modules=MODULES, globals_=globals()) # instantiate AMPL object and register magics

In the list ``MODULES`` you can specify the AMPL solvers you want to use in your notebook.
As a quick-start you can use our template notebook: :ref:`tag-template`.
You can contribute to this repository by making pull requests to https://github.com/ampl/amplcolab and following the instructions in the  `README <https://github.com/ampl/amplcolab/blob/master/README.md>`_ file.

.. code-block:: python

    # Full list of modules available
    MODULES = ["amplgsl", "baron", "cbc", "coin", "conopt", "copt", "cplex", "gokestrel", "gurobi", "highs", "knitro", "lgo", "lindoglobal", "loqo", "minos", "octeract", "open", "plugins", "snopt", "xpress"]

.. note::

    In these notebooks there are ``%%ampl_eval`` cells that allow you to run AMPL code directly from the notebook. 
    They are equivalent to ``ampl.eval(\"\"\"cell content\"\"\")``.

.. warning::
    Some notebooks require commercial solvers. You can use a free `AMPL Community
    Edition <https://ampl.com/ce/>`_ license with an open-source solver (e.g., HiGHS, CBC, Couenne, Ipopt, Bonmin)
    or with a commercial solver from the `NEOS Server <http://www.neos-server.org/>`_ as described in https://dev.ampl.com/solvers/kestrel.html.
    In the list ``MODULES`` you need to include 
    ``"gokestrel"`` to use the `kestrel <https://dev.ampl.com/solvers/kestrel.html>`_ driver; 
    ``"highs"`` for the `HiGHS <https://highs.dev/>`_ solver; 
    ``"coin"`` for the `COIN-OR <https://www.coin-or.org/>`_ solvers.
    To use other commercial solvers without NEOS, your license needs to include the commercial solver.
 

Main categories
---------------

.. toctree::
    :maxdepth: 1

    tags/ampl-lecture
    tags/finance
    tags/industry
    tags/military
    tags/google-sheets

Authors
-------

The notebooks in this repository are contributed by the following authors:

.. toctree::
    :maxdepth: 2

    authors/index

**Your name can be here too!** Just make a pull request to https://github.com/ampl/amplcolab.

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
    print("\n" + "\n".join(badges) + "\n", file=fout)
    description = info.get("description", None)
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
        print(f"| Author: {', '.join(lst)}\n", file=fout)


madeby = {}
tagged = {}
names = {}
for info in NOTEBOOKS:
    title, fname = info["title"], info["fname"]
    print(f"Getting tags and authors of {fname}")
    for tag in info.get("tags", []):
        if tag not in tagged:
            tagged[tag] = []
        tagged[tag].append(info)
    for author in info.get("notebook_author", "").split(","):
        author = author.strip()
        if "<" not in author:
            continue
        assert "<<" in author and ">>" in author
        email = author[author.find("<<") + 2 : author.rfind(">>")].strip()
        name = author[: author.find("<<")].strip()
        if email not in madeby:
            madeby[email] = []
            names[email] = name
        madeby[email].append(info)

    print_markdown(info, readme)
    print_rst(info, index)


print(
    """
Tag list
--------

.. toctree::
    :maxdepth: 2

    tags/index
""",
    file=index,
)

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
    :maxdepth: 2

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

The notebooks in this repository are contributed by the following authors:

.. toctree::
    :maxdepth: 1

"""
authors_sorted = sorted(((name, email) for email, name in names.items()))
for _, email in authors_sorted:
    email = email.lower().replace("@", "_at_")
    authors_index += f"    {email}\n"
authors_index += """
**Your name can be here too!** Just make a pull request to https://github.com/ampl/amplcolab.
"""
print(authors_index, file=open(f"docs/source/authors/index.rst", "w"))

for name, email in authors_sorted:
    print(f">>{name} <{email}>")
    lst = madeby[email]
    email = email.replace("@", "_at_")
    email_rst = open(f"docs/source/authors/{email}.rst", "w")
    title = f"{name} ({len(lst)} notebook{'s' if len(lst) > 1 else ''})"
    title += "\n" + "=" * len(title) + "\n"
    header = f".. _email-{email}:\n\n{title}"
    print(header, file=email_rst)
    for info in lst:
        print_rst(info, email_rst)
