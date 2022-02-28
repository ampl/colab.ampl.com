import os

NOTEBOOKS = {
    'Google Hashcode 2022': 'miscellaneous/hashcode/practice_problem.ipynb',
    'Jupyter Notebook Integration': 'miscellaneous/magics.ipynb',
    'Roll Cutting - Revision 1 & 2': 'miscellaneous/pattern_tradeoff.ipynb',
    'Google Colab & Kaggle Template': 'miscellaneous/colab.ipynb',
    'Setup & Quick Start': 'miscellaneous/quickstart.ipynb',
    'Pattern Enumeration': 'miscellaneous/pattern_enumeration.ipynb',
    'Pattern Generation': 'miscellaneous/pattern_generation.ipynb',
    'Using Google Sheets': 'miscellaneous/gspread.ipynb',
    'Calculate efficient frontier (uses Google Sheets)': 'finance/efficient_frontier.ipynb',
    'Optimization Methods in Finance: Chapter 3': 'finance/finance_opt_example_3_1.ipynb',
}

GITHUB_PATH = 'ampl/amplcolab/blob/master/'


def github_column(fname):
    basename = os.path.basename(fname)
    url = f'github.com/{GITHUB_PATH}/{fname}'.replace('//', '/')
    return f'[{basename}](https://{url})'


def colab_column(fname):
    prefix = 'colab.research.google.com/github'
    url = f'{prefix}/{GITHUB_PATH}/{fname}'.replace('//', '/')
    return f'[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://{url})'


def kaggle_column(fname):
    prefix = 'kaggle.com/kernels/welcome?src=https://github.com'
    url = f'{prefix}/{GITHUB_PATH}/{fname}'.replace('//', '/')
    return f'[![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://{url})'


def gradient_column(fname):
    prefix = 'console.paperspace.com/github'
    url = f'{prefix}/{GITHUB_PATH}/{fname}'.replace('//', '/')
    return f'[![Gradient](https://assets.paperspace.io/img/gradient-badge.svg)](https://{url})'


def sagemaker_column(fname):
    prefix = 'studiolab.sagemaker.aws/import/github'
    url = f'{prefix}/{GITHUB_PATH}/{fname}'.replace('//', '/')
    return f'[![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://{url})'


print('''
# Jupyter Notebooks
| Title  |  File  |  Colab | Kaggle | Gradient | SageMaker|
|--------|--------|--------|--------|----------|----------|''')

for title, fname in NOTEBOOKS.items():
    notebook = open(fname, 'r').read()
    colab_only = ' gspread' in notebook

    github = github_column(fname)
    colab = colab_column(fname)
    kaggle = kaggle_column(fname) if not colab_only else ''
    gradient = gradient_column(fname) if not colab_only else ''
    sagemaker = sagemaker_column(fname) if not colab_only else ''
    print(f'|{title}|{github}|{colab}|{kaggle}|{gradient}|{sagemaker}|')
