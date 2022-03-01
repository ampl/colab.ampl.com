import json
from utils import (list_notebooks, github_badge, colab_badge,
                   kaggle_badge, gradient_badge, sagemaker_badge)

NOTEBOOKS = list_notebooks()

for title, fname in sorted(NOTEBOOKS.items()):
    print(f'{fname}: {title}')
    notebook = open(fname, 'r').read()
    data = json.loads(notebook)
    cells = data['cells']
    assert cells[0]['cell_type'] == 'markdown'
    header = cells[0]['source']
    assert header[0].startswith('#')

    # Remove old badges
    header = [row for row in header if not row.startswith('[![')]
    remove = []
    for i, row in enumerate(header):
        if row == '\n' and header[i-1] == '\n':
            remove.append(i)
    for i in reversed(remove):
        print('removing', i)
        del header[i]

    cells[0]['source'] = header

    colab_only = ' gspread' in notebook
    github = github_badge(fname)
    colab = colab_badge(fname)
    kaggle = kaggle_badge(fname) if not colab_only else ''
    gradient = gradient_badge(fname) if not colab_only else ''
    sagemaker = sagemaker_badge(fname) if not colab_only else ''

    badges = f'{github}{colab}{kaggle}{gradient}{sagemaker}\n'
    header.insert(1, '\n')
    header.insert(1, badges)

    open(fname, 'w').write(json.dumps(data))
