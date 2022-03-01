import os
import re
import json

lst = [
    os.path.join(dirpath, fname)[2:]
    for (dirpath, _, files) in os.walk('.')
    for fname in files
    if fname.endswith('.ipynb') and '.ipynb_checkpoints' not in dirpath
]

NOTEBOOKS = {}
for fname in lst:
    print(f'Processing: {fname}')
    data = json.load(open(fname, 'r'))
    cells = data['cells']
    assert cells[0]['cell_type'] == 'markdown'
    header = cells[0]['source']
    assert header[0].startswith('#')
    title = header[0].lstrip('# ')
    NOTEBOOKS[title] = fname
    print(f'Title: {title}')

GITHUB_PATH = 'ampl/amplcolab/blob/master/'


def normalize(url):
    return re.sub(r'([^:])//+', r'\1/', url)


def github_column(fname, rst=False):
    basename = os.path.basename(fname)
    image = 'https://img.shields.io/badge/github-%23121011.svg?logo=github'
    url = normalize(f'https://github.com/{GITHUB_PATH}/{fname}')
    if not rst:
        return f'[![{basename}]({image})]({url})'
    return f'''.. image:: {image}
    :target: {url}
    :alt: {basename}
    '''


def colab_column(fname, rst=False):
    prefix = 'https://colab.research.google.com/github'
    image = 'https://colab.research.google.com/assets/colab-badge.svg'
    url = normalize(f'{prefix}/{GITHUB_PATH}/{fname}')
    if not rst:
        return f'[![Open In Colab]({image})]({url})'
    return f'''.. image:: {image}
    :target: {url}
    :alt: Open In Colab
    '''


def kaggle_column(fname, rst=False):
    prefix = 'https://kaggle.com/kernels/welcome?src=https://github.com'
    image = 'https://kaggle.com/static/images/open-in-kaggle.svg'
    url = normalize(f'{prefix}/{GITHUB_PATH}/{fname}')
    if not rst:
        return f'[![Kaggle]({image})]({url})'
    return f'''.. image:: {image}
    :target: {url}
    :alt: Kaggle
    '''


def gradient_column(fname, rst=False):
    prefix = 'https://console.paperspace.com/github'
    image = 'https://assets.paperspace.io/img/gradient-badge.svg'
    url = normalize(f'{prefix}/{GITHUB_PATH}/{fname}')
    if not rst:
        return f'[![Gradient]({image})]({url})'
    return f'''.. image:: {image}
    :target: {url}
    :alt: Gradient
    '''


def sagemaker_column(fname, rst=False):
    prefix = 'https://studiolab.sagemaker.aws/import/github'
    image = 'https://studiolab.sagemaker.aws/studiolab.svg'
    url = normalize(f'{prefix}/{GITHUB_PATH}/{fname}')
    if not rst:
        return f'[![Open In SageMaker Studio Lab]({image})]({url})'
    return f'''.. image:: {image}
    :target: {url}
    :alt: Open In SageMaker Studio Lab
    '''


readme = open('README.md', 'w')
index = open('docs/source/index.rst', 'w')

print('''# AMPL Model Colaboratory

| Title  |  GitHub  |  Colab | Kaggle | Gradient | SageMaker|
|--------|--------|--------|--------|----------|----------|''', file=readme)

print('''
AMPL Model Colaboratory
=======================

''', file=index)

for title, fname in sorted(NOTEBOOKS.items()):
    notebook = open(fname, 'r').read()
    colab_only = ' gspread' in notebook

    github = github_column(fname)
    colab = colab_column(fname)
    kaggle = kaggle_column(fname) if not colab_only else ''
    gradient = gradient_column(fname) if not colab_only else ''
    sagemaker = sagemaker_column(fname) if not colab_only else ''
    print(f'|{title}|{github}|{colab}|{kaggle}|{gradient}|{sagemaker}|', file=readme)

    github = github_column(fname, rst=True)
    colab = colab_column(fname, rst=True)
    kaggle = kaggle_column(fname, rst=True) if not colab_only else ''
    gradient = gradient_column(fname, rst=True) if not colab_only else ''
    sagemaker = sagemaker_column(fname, rst=True) if not colab_only else ''
    print(title + '\n' + '-'*len(title), file=index)
    print(f'{github}\n{colab}\n{kaggle}\n{gradient}\n{sagemaker}\n', file=index)
