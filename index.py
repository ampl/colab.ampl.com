from utils import (list_notebooks, github_badge, colab_badge,
                   kaggle_badge, gradient_badge, sagemaker_badge)

NOTEBOOKS = list_notebooks()


readme = open('README.md', 'w')
index = open('docs/source/index.rst', 'w')

print('''# AMPL Model Colaboratory

| Title  | GitHub |  Colab | Kaggle | Gradient | SageMaker|
|--------|--------|--------|--------|----------|----------|''', file=readme)

print('''
AMPL Model Colaboratory
=======================

Tags
----

.. toctree::
    :maxdepth: 2

    tag-ampl-only
    tag-amplpy
    tag-example
    tag-finance
    tag-google-sheets
    tag-industry
    tag-template

Notebooks
---------

''', file=index)


def print_markdown(info, fout):
    fname = info['fname']
    colab_only = info['colab_only']
    github = github_badge(fname)
    colab = colab_badge(fname)
    kaggle = kaggle_badge(fname) if not colab_only else ''
    gradient = gradient_badge(fname) if not colab_only else ''
    sagemaker = sagemaker_badge(fname) if not colab_only else ''
    print(f'|{title}|{github}|{colab}|{kaggle}|{gradient}|{sagemaker}|', file=fout)


def print_rst(info, fout):
    fname, title = info['fname'], info['title']
    colab_only = info['colab_only']
    github = github_badge(fname, rst=True)
    colab = colab_badge(fname, rst=True)
    kaggle = kaggle_badge(fname, rst=True) if not colab_only else ''
    gradient = gradient_badge(fname, rst=True) if not colab_only else ''
    sagemaker = sagemaker_badge(fname, rst=True) if not colab_only else ''
    print(title + '\n' + '^'*len(title), file=fout)
    description = info.get('description', None)
    if description:
        print(f'Description: {description}\n', file=fout)
    tags = info.get('tags', None)
    if tags:
        print(f'Tags: {", ".join(tags)}\n', file=fout)
    author = info.get('notebook_author', None)
    if author:
        print(f'Author: {author}\n', file=fout)
    print(f'{github}\n{colab}\n{kaggle}\n{gradient}\n{sagemaker}\n', file=fout)


tagged = {}
for info in NOTEBOOKS:
    title, fname = info['title'], info['fname']
    for tag in info.get('tags', []):
        if tag not in tagged:
            tagged[tag] = []
        tagged[tag].append(info)

    print_markdown(info, readme)
    print_rst(info, index)


for tag in tagged:
    tag_rst = open(f'docs/source/tag-{tag}.rst', 'w')
    title = f'{tag}'
    title += '\n' + '='*len(title) + '\n'
    print(title, file=tag_rst)
    for info in tagged[tag]:
        print_rst(info, tag_rst)
