#!/bin/bash
python get_tabelle.py ../source/_static/xlsx/
python create_sphinx_tables.py ../source/_static/xlsx/ ../source/
