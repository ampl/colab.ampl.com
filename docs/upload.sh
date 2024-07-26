#!/bin/bash
cd "`dirname "$0"`"
set -ex
source venv/bin/activate
make html
rsync -av --delete build/html/ kinsta-staging:/www/amplnewsitestaging_483/public/colab
rsync -av --delete build/html/ kinsta:/www/amplnewsitestaging_483/public/colab
