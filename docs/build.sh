rm -rf xlsx/*
rm -rf _includes/tabelle/*
rm -rf _posts/*-tab_*

python bin/get_tabelle.py
python bin/create_jekyll_posts.py xlsx/ _includes/tabelle/
