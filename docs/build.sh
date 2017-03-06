pip install -r bin/requirements.txt
rm -rf xlsx/*
rm -rf _includes/tabelle/*
rm -rf _posts/*-tab_*
rm -rf _posts/*-sec_*
rm -rf _posts/*-error_*

python bin/get_tabelle.py
python bin/create_jekyll_posts.py xlsx/ _includes/tabelle/
