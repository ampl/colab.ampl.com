import os
import re
import json


def list_notebooks():
    lst = [
        os.path.join(dirpath, fname)[2:]
        for (dirpath, _, files) in os.walk('.')
        for fname in files
        if fname.endswith('.ipynb') and '.ipynb_checkpoints' not in dirpath
    ]

    notebooks = {}
    for fname in lst:
        print(f'Processing: {fname}')
        data = json.load(open(fname, 'r'))
        cells = data['cells']
        assert cells[0]['cell_type'] == 'markdown'
        header = cells[0]['source']
        assert header[0].startswith('#')
        title = header[0].lstrip('# ').rstrip('\n')
        notebooks[title] = fname
        print(f'Title: {title}\n')
    return notebooks


GITHUB_PATH = 'ampl/amplcolab/blob/master/'


def normalize(url):
    return re.sub(r'([^:])//+', r'\1/', url)


def github_badge(fname, rst=False):
    basename = os.path.basename(fname)
    image = 'https://img.shields.io/badge/github-%23121011.svg?logo=github'
    url = normalize(f'https://github.com/{GITHUB_PATH}/{fname}')
    if not rst:
        return f'[![{basename}]({image})]({url})'
    return f'''.. image:: {image}
    :target: {url}
    :alt: {basename}
    '''


def colab_badge(fname, rst=False):
    prefix = 'https://colab.research.google.com/github'
    image = 'https://colab.research.google.com/assets/colab-badge.svg'
    url = normalize(f'{prefix}/{GITHUB_PATH}/{fname}')
    if not rst:
        return f'[![Open In Colab]({image})]({url})'
    return f'''.. image:: {image}
    :target: {url}
    :alt: Open In Colab
    '''


def kaggle_badge(fname, rst=False):
    prefix = 'https://kaggle.com/kernels/welcome?src=https://github.com'
    image = 'https://kaggle.com/static/images/open-in-kaggle.svg'
    url = normalize(f'{prefix}/{GITHUB_PATH}/{fname}')
    if not rst:
        return f'[![Kaggle]({image})]({url})'
    return f'''.. image:: {image}
    :target: {url}
    :alt: Kaggle
    '''


def gradient_badge(fname, rst=False):
    prefix = 'https://console.paperspace.com/github'
    image = 'https://assets.paperspace.io/img/gradient-badge.svg'
    url = normalize(f'{prefix}/{GITHUB_PATH}/{fname}')
    if not rst:
        return f'[![Gradient]({image})]({url})'
    return f'''.. image:: {image}
    :target: {url}
    :alt: Gradient
    '''


def sagemaker_badge(fname, rst=False):
    prefix = 'https://studiolab.sagemaker.aws/import/github'
    image = 'https://studiolab.sagemaker.aws/studiolab.svg'
    url = normalize(f'{prefix}/{GITHUB_PATH}/{fname}')
    if not rst:
        return f'[![Open In SageMaker Studio Lab]({image})]({url})'
    return f'''.. image:: {image}
    :target: {url}
    :alt: Open In SageMaker Studio Lab
    '''
