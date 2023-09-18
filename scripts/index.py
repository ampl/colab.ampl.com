from utils import list_notebooks, list_badges
from headers import update_notebook_headers
import glob
import os

update_notebook_headers()

os.chdir(os.path.dirname(__file__) or os.curdir)
os.chdir("..")

NOTEBOOKS = list_notebooks()


readme = open("README.md", "w", newline="\n")
index = open("docs/source/index.rst", "w", newline="\n")
gettingstarted = open("docs/source/getting-started.rst", "w", newline="\n")
notebooks = open("docs/source/notebooks.rst", "w", newline="\n")

print(
    """# AMPL Model Colaboratory

## Website

https://colab.ampl.com

## Contribution Guide

1. Use the template [template/colab.ipynb](https://github.com/ampl/colab.ampl.com/blob/master/template/colab.ipynb) as base template.

2. In the header make sure you fill the following fields:
```
Description: <required>

Tags: <required>, <>, <>

Notebook author: <required>

Model author: <optional>

License: <optional>

References: <optional>
```

3. Do not modify the initial two cells that take care of setup and jupyter notebook integration
to do anything other than installing packages and instantiating the ampl_notebook. You can modify
the list of modules and add more dependencies, but if you do anything else the changes may be overwritten.

4. Place your notebook inside `colab.ampl.com/authors/<github_username>/`.

5. Update the badges and the index as shown below before committing.

Note: The default license for every notebook is [MIT](https://github.com/ampl/colab.ampl.com/blob/master/LICENSE) unless specified otherwise in the notebook.

### Updating notebook headers & index

The following commands update the README file and the index in the documentation, as well as add any new automatically created files to the repository:
```bash
$ python scripts/index.py
$ git add docs/source/
```

Note that the notebook headers are patched with new badges using links to the correct locations after the notebook is published.
The first two notebook cells are modified to ensure that requirements are installed and that the ampl_notebook is instantiated.

## Notebooks

| Title  | GitHub |  Colab | Kaggle | Gradient | SageMaker|
|--------|--------|--------|--------|----------|----------|""",
    file=readme,
)

print(
    """
AMPL Model Colaboratory
=======================

AMPL Model Colaboratory is a collection of AMPL models in `Jupyter Notebooks <https://jupyter.org/>`_
that run on platforms such as **Google Colab**, **Kaggle**, **Gradient**, and **AWS SageMaker**.
[:ref:`See our Highlights <tag-highlights>`]

.. raw:: html

    <a href="https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/glebbelov/miscellaneous/nqueens.ipynb" target="_blank">
        <video width="100%" autoplay loop muted poster="https://ampl.com/upload/videos/nqueens_poster.jpg">
            <source src="https://ampl.com/upload/videos/nqueens.mp4" type="video/mp4" />
        </video>
    </a>

.. grid:: 1 1 2 2
    :gutter: 0
    :margin: 0
    :padding: 0

    .. grid-item-card::
        :margin: 0
        :padding: 0

        You can use the **Christmas notebook** written by `ChatGPT <https://chat.openai.com/>`_ to get started:

        .. image:: https://colab.research.google.com/assets/colab-badge.svg
            :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/chatgpt/christmas.ipynb
            :alt: Open In Colab

        .. image:: https://kaggle.com/static/images/open-in-kaggle.svg
            :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/chatgpt/christmas.ipynb
            :alt: Kaggle

        .. image:: https://assets.paperspace.io/img/gradient-badge.svg
            :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/chatgpt/christmas.ipynb
            :alt: Gradient

        .. image:: https://studiolab.sagemaker.aws/studiolab.svg
            :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/chatgpt/christmas.ipynb
            :alt: Open In SageMaker Studio Lab

        | BTW: you can even ask `ChatGPT <https://chat.openai.com/>`_ to write models for you! If it makes mistakes you can ask for help in our new `Discourse Forum <https://discuss.ampl.com>`_!

    .. grid-item-card::
        :margin: 0
        :padding: 0

        .. figure:: /_static/3lines.png
            :alt: the only 3 lines you need to use AMPL on Colab
            :align: center
            :width: 100%
            :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/template/minimal.ipynb

Contents
--------

.. toctree::
    :maxdepth: 2

    getting-started
    modules/index
    Highlights <tags/highlights>
    Lectures <tags/ampl-lecture>
    authors/index

.. toctree::
    :hidden:

    tags/index
    notebooks

Notebooks
---------

""",
    file=index,
)

print(
    """
Getting Started
===============

Quick setup
-----------

In order to be use AMPL on any notebook platform (e.g., Google Colab) you just need the following two code blocks
at the beginning of your notebook:

.. code-block:: bash

   # Install dependencies
   %pip install -q amplpy


.. code-block:: python

    # Google Colab & Kaggle integration
    from amplpy import AMPL, ampl_notebook

    ampl = ampl_notebook(
        modules=["coin", "highs", "gokestrel"],  # modules to install
        license_uuid="your-license-uuid",  # license to use
    )  # instantiate AMPL object and register magics

In the list ``modules`` you can specify the AMPL solvers you want to use in your notebook.
For more information on the AMPL Modules for Python see `Python Modules Documentation <https://dev.ampl.com/ampl/python/modules.html>`_.
For more information on how to use ``amplpy`` see `Python API Documentation <https://amplpy.readthedocs.io/>`_.

.. grid:: 1 1 2 2
    :gutter: 0
    :margin: 0
    :padding: 0

    .. grid-item-card::
        :margin: 0
        :padding: 0

        Quick Start using Pandas dataframes
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        Data can be loaded in various forms, one of which is ``pandas.DataFrame`` objects.

        .. image:: https://colab.research.google.com/assets/colab-badge.svg
            :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/pandasdiet.ipynb
            :alt: Open In Colab

        .. image:: https://kaggle.com/static/images/open-in-kaggle.svg
            :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/pandasdiet.ipynb
            :alt: Kaggle

        .. image:: https://assets.paperspace.io/img/gradient-badge.svg
            :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/pandasdiet.ipynb
            :alt: Gradient

        .. image:: https://studiolab.sagemaker.aws/studiolab.svg
            :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/pandasdiet.ipynb
            :alt: Open In SageMaker Studio Lab

    .. grid-item-card::
        :margin: 0
        :padding: 0

        Quick Start using lists and dictionaries
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        Data can be loaded in various forms, including Python lists and dictionaries.

        .. image:: https://colab.research.google.com/assets/colab-badge.svg
            :target: https://colab.research.google.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/nativediet.ipynb
            :alt: Open In Colab

        .. image:: https://kaggle.com/static/images/open-in-kaggle.svg
            :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/nativediet.ipynb
            :alt: Kaggle

        .. image:: https://assets.paperspace.io/img/gradient-badge.svg
            :target: https://console.paperspace.com/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/nativediet.ipynb
            :alt: Gradient

        .. image:: https://studiolab.sagemaker.aws/studiolab.svg
            :target: https://studiolab.sagemaker.aws/import/github/ampl/colab.ampl.com/blob/master/authors/fdabrandao/quick-start/nativediet.ipynb
            :alt: Open In SageMaker Studio Lab

.. note::

    In these notebooks there are ``%%ampl_eval`` cells that allow you to run AMPL code directly from the notebook. 
    They are equivalent to ``ampl.eval(\"\"\"cell content\"\"\")``.

Learn more: [`Python Modules Documentation <https://dev.ampl.com/ampl/python/modules.html>`_] [`Python API Documentation <https://amplpy.readthedocs.io/>`_]

AMPL is free on Colab
---------------------

- On **Google Colab** there is a default `AMPL Community Edition license <https://ampl.com/ce/>`_
  that gives you **unlimited access to AMPL
  with open-source solvers** (e.g., HiGHS, CBC, Couenne, Ipopt, Bonmin)
  or with commercial solvers from the `NEOS Server <https://www.neos-server.org/>`_ as described in `Kestrel documentation <https://dev.ampl.com/solvers/kestrel.html>`_.

- `AMPL for Courses <https://ampl.com/licenses-and-pricing/ampl-for-teaching/>`_ is another free license of full-featured AMPL with no limitations on problem size, and a selection of popular commercial and open-source solvers.
  **This license can be used on Google Colab and similar platforms for teaching.**

- To access commercial solvers you can use solver trials associated with your `AMPL Community Edition license <https://ampl.com/ce/>`_.

Learn more: [`AMPL Community Edition <https://ampl.com/ce/>`_] [`AMPL for Courses <https://ampl.com/licenses-and-pricing/ampl-for-teaching/>`_]

AMPL Python API: amplpy
-----------------------

`amplpy <https://amplpy.readthedocs.io>`_ is an interface that allows developers to access the features of `AMPL <https://ampl.com>`_ from within Python.
For a quick introduction to AMPL see `Quick Introduction to AMPL <https://dev.ampl.com/ampl/introduction.html>`_.

In the same way that AMPL's syntax matches naturally the mathematical description of the model,
the input and output data matches naturally Python lists, sets, dictionaries, ``pandas`` and ``numpy`` objects.

All model generation and solver interaction is handled directly by AMPL, which leads to
great stability and speed; the library just acts as an intermediary, and the added overhead (in terms of memory and
CPU usage) depends mostly on how much data is sent and read back from AMPL, the size of the expanded model as such is irrelevant.

With `amplpy <https://amplpy.readthedocs.io>`_ you can model and solve large scale optimization problems in Python with the performance of heavily optimized C code
without losing model readability. The same model can be deployed on applications
built on different languages by just switching the API used.

Learn more: [`Python API Documentation <https://amplpy.readthedocs.io>`_]
""",
    file=gettingstarted,
)


print(
    """
Notebooks
=========

""",
    file=notebooks,
)


def print_markdown(info, fout):
    fname = info["fname"]
    colab_only = info["colab_only"]
    badges = list_badges(fname, colab_only, page="README")
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


nb_madeby = {}
nb_tagged = {}
nb_uses = {}
nb_names = {}
for info in NOTEBOOKS:
    title, fname, modules = info["title"], info["fname"], info["modules"]
    print(f"Getting tags, authors, and modules of {fname}")
    for mod in modules:
        if mod not in nb_uses:
            nb_uses[mod] = []
        nb_uses[mod].append(info)
    for tag in info.get("tags", []):
        if tag not in nb_tagged:
            nb_tagged[tag] = []
        nb_tagged[tag].append(info)
    for author in info.get("notebook_author", "").split(","):
        author = author.strip()
        if "<" not in author:
            continue
        assert "<<" in author and ">>" in author
        email = author[author.find("<<") + 2 : author.rfind(">>")].strip()
        name = author[: author.find("<<")].strip()
        if email not in nb_madeby:
            nb_madeby[email] = []
            nb_names[email] = name
        nb_madeby[email].append(info)

    print_markdown(info, readme)
    print_rst(info, index)
    print_rst(info, notebooks)

print(
    """## License

MIT

***
Copyright © 2022-2023 AMPL Optimization inc. All rights reserved.
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
for tag, lst in sorted(nb_tagged.items()):
    label = f"{tag} ({len(lst)} notebook{'s' if len(lst) > 1 else ''}) <{tag}>"
    tags_index += f"    {label}\n"
print(tags_index, file=open(f"docs/source/tags/index.rst", "w"))

for tag, lst in nb_tagged.items():
    tag_rst = open(f"docs/source/tags/{tag}.rst", "w")
    title = f"{tag}"
    title += "\n" + "=" * len(title) + "\n"
    header = f".. _tag-{tag}:\n\n{title}"
    print(header, file=tag_rst)
    for info in lst:
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
authors_sorted = sorted(((name, email) for email, name in nb_names.items()))
for _, email in authors_sorted:
    email = email.lower().replace("@", "_at_")
    authors_index += f"    {email}\n"
authors_index += """

.. note::
    **Your name can be here too!** Just make a pull request to https://github.com/ampl/colab.ampl.com or
    send a link to your notebook by email to devteam@ampl.com.

Contribution Guide
------------------

1. Use the template
   `template/colab.ipynb <https://github.com/ampl/colab.ampl.com/blob/master/template/colab.ipynb>`__
   as base template.

2. In the header make sure you fill the following fields:

::

   Description: <required>

   Tags: <required>, <>, <>

   Notebook author: <required>

   Model author: <optional>

   License: <optional>

   References: <optional>

3. Do not modify the initial two cells that take care of setup and
   jupyter notebook integration to do anything other than installing
   packages and instantiating the ampl_notebook. You can modify the list
   of modules and add more dependencies, but if you do anything else the
   changes may be overwritten.

4. Place your notebook inside ``colab.ampl.com/authors/<github_username>/``.

5. Update the badges and the index as shown below before committing.

Note: The default license for every notebook is
`MIT <https://github.com/ampl/colab.ampl.com/blob/master/LICENSE>`__ unless
specified otherwise in the notebook.

Updating notebook headers & index
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following commands update the README file and the index in the
documentation, as well as add any new automatically created files:

.. code:: bash

   $ python scripts/index.py
   $ git add docs/source/

Note that the notebook headers are patched with new badges using links
to the correct locations after the notebook is published. The first two
notebook cells are modified to ensure that requirements are installed
and that the ampl_notebook is instantiated.
"""
print(authors_index, file=open(f"docs/source/authors/index.rst", "w"))

for name, email in authors_sorted:
    print(f">>{name} <{email}>")
    lst = nb_madeby[email]
    email = email.replace("@", "_at_")
    email_rst = open(f"docs/source/authors/{email}.rst", "w")
    title = f"{name} ({len(lst)} notebook{'s' if len(lst) > 1 else ''})"
    title += "\n" + "=" * len(title) + "\n"
    header = f".. _email-{email}:\n\n{title}"
    print(header, file=email_rst)
    for info in lst:
        print_rst(info, email_rst)

# Modules

for f in glob.glob("docs/source/modules/*.rst"):
    os.remove(f)
modules_index = """
Modules
=======

Modules available
-----------------

`AMPL and all Solvers are now available as Python Packages. <https://dev.ampl.com/ampl/python/modules.html>`_
List of modules available:

- Open-source: ``highs``, ``cbc``, ``coin`` (includes: CBC, Couenne, Ipopt, Bonmin), ``open`` (includes all open-source solvers)
- `NEOS Server <https://www.neos-server.org/>`_: ``gokestrel`` (`kestrel client <https://dev.ampl.com/solvers/kestrel.html>`_)
- Commercial solvers: ``baron``, ``conopt``, ``copt``, ``cplex``, ``gurobi``, ``knitro``, ``lgo``, ``lindoglobal``, ``loqo``, ``minos``, ``mosek``, ``octeract``, ``snopt``, ``xpress``
- AMPL Plugins: ``amplgsl`` (`amplgsl docs <https://amplgsl.readthedocs.io/>`_), ``plugins`` (`amplplugins docs <https://amplplugins.readthedocs.io/>`_)

.. note::
    On Google Colab there is a default `AMPL Community
    Edition license <https://ampl.com/ce/>`_ that gives you **unlimited access to AMPL
    with open-source solvers** (e.g., HiGHS, CBC, Couenne, Ipopt, Bonmin)
    or with commercial solvers from the `NEOS Server <https://www.neos-server.org/>`_ as described in `Kestrel documentation <https://dev.ampl.com/solvers/kestrel.html>`_.
    
    In the list ``modules`` you need to include 
    ``"gokestrel"`` to use the `kestrel <https://dev.ampl.com/solvers/kestrel.html>`_ driver; 
    ``"highs"`` for the `HiGHS <https://highs.dev/>`_ solver; 
    ``"coin"`` for the `COIN-OR <https://www.coin-or.org/>`_ solvers.
    To use other commercial solvers, your license needs to include the commercial solver (e.g., an AMPL CE commercial solver trial).
    
    .. code-block:: bash

        # Install dependencies
        %pip install -q amplpy

    .. code-block:: python

        # Google Colab & Kaggle integration
        from amplpy import AMPL, ampl_notebook

        ampl = ampl_notebook(
            modules=["gurobi", "coin", "highs", "gokestrel"],  # modules to install
            license_uuid="default",  # license to use
        )  # instantiate AMPL object and register magics

Learn more: [`AMPL and Solvers modules <https://dev.ampl.com/ampl/python/modules.html>`_] [`Solver docs <https://dev.ampl.com/solvers/index.html>`_]

Notebooks grouped by modules
----------------------------

.. toctree::
    :maxdepth: 2

"""
for mod in sorted(nb_uses):
    modules_index += f"    {mod}\n"
print(modules_index, file=open(f"docs/source/modules/index.rst", "w"))

for mod, lst in nb_uses.items():
    mod_rst = open(f"docs/source/modules/{mod}.rst", "w")
    title = f"{mod} ({len(lst)} notebook{'s' if len(lst) > 1 else ''})"
    title += "\n" + "=" * len(title) + "\n"
    header = f".. _module-{mod}:\n\n{title}"
    print(header, file=mod_rst)
    for info in lst:
        print_rst(info, mod_rst)
