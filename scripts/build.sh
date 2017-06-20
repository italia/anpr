#!/bin/bash

cwd=$(pwd)
echo $cwd #script folder

#cd /tmp/
#rm -rf ANPR_subentro
#git clone https://github.com/vintra73/ANPR_subentro.git
#cp -rf ANPR_subentro/src $cwd/../src/subentro

cd $cwd
pip install -r requirements.txt
rm -rf ../src/tab/tab_*
python crawl_contents.py ../src/_static/xlsx/ ../src/tab/

cd ..
make clean html
open docs/index.html
