#!/bin/bash
python crawl_contents.py ../src/_static/xlsx/ ../src/
cd ..
make html 

#rm ../src/tab_Comuni.rst
