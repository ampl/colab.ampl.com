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

Notebooks
---------

''', file=index)

for title, fname in sorted(NOTEBOOKS.items()):
    notebook = open(fname, 'r').read()
    colab_only = ' gspread' in notebook

    github = github_badge(fname)
    colab = colab_badge(fname)
    kaggle = kaggle_badge(fname) if not colab_only else ''
    gradient = gradient_badge(fname) if not colab_only else ''
    sagemaker = sagemaker_badge(fname) if not colab_only else ''
    print(f'|{title}|{github}|{colab}|{kaggle}|{gradient}|{sagemaker}|', file=readme)

    github = github_badge(fname, rst=True)
    colab = colab_badge(fname, rst=True)
    kaggle = kaggle_badge(fname, rst=True) if not colab_only else ''
    gradient = gradient_badge(fname, rst=True) if not colab_only else ''
    sagemaker = sagemaker_badge(fname, rst=True) if not colab_only else ''
    print(title + '\n' + '^'*len(title), file=index)
    print(f'{github}\n{colab}\n{kaggle}\n{gradient}\n{sagemaker}\n', file=index)
