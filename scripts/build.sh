#!/bin/bash
pip install -r requirements.txt
python crawl_contents.py ../src/_static/xlsx/ ../src/
cd ..
make html
open docs/index.html
#rm ../src/tab_Comuni.rst
