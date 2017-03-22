#!/bin/bash
python get_tabelle.py
python create_sphinx_tables.py xlsx/ ../source/
