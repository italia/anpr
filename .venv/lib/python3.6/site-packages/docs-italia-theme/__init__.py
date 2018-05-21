"""Docs Italia theme - Team Digitale"""

import os
import re
import yaml

# This part would be better placed as an extension:
# It loads yaml data files to set them as variables
def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return cur_dir


def deep_merge(source, destination):
    """Deep merge dictionaries"""
    for key, value in source.items():
        if isinstance(value, dict):
            node = destination.setdefault(key, {})
            deep_merge(value, node)
        else:
            destination[key] = value
    return destination


def load_site_data():
    """Load data from Team Digitale Jekyll site config"""
    source_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'data')
    )
    config_path = os.path.join(source_path, '_config.yml')
    data_path = os.path.join(source_path, '_data')
    context = {}

    # Load site config
    config_h = open(config_path)
    config_data = yaml.load(config_h)
    context.update(config_data)

    # Load Jekyll data files
    filename_re = re.compile('\.yml$')
    context['data'] = {}
    for filename in os.listdir(data_path):
        if filename_re.search(filename):
            datafile_source = filename_re.sub('', filename)
            datafile_path = os.path.join(data_path, filename)
            datafile_h = open(datafile_path)
            datafile_data = yaml.load(datafile_h)
            context['data'].update({datafile_source: datafile_data})

    # Transform network links to ordered mapping. Doing this dynamically
    # instead of with overrides to alter mapping into an ordered list and keep
    # the existing data
    network_links = []
    for link in ['trasformazione_digitale', 'developers', 'design', 'forum',
                 'docs', 'github']:
        link_data = context['data']['network_links'].get(link, {}).copy()
        link_data['name'] = link

        # Alter classes
        class_str = link_data.get('class', '')
        classes = class_str.split(' ')
        try:
            del classes[classes.index('current')]
        except (IndexError, ValueError):
            pass
        if link == 'docs':
            classes.append('current')
        link_data['class'] = ' '.join(classes)

        network_links.append(link_data)
    context['data']['network_links'] = network_links

    footer_links = []
    for link in ['privacy', 'legal']:
        link_data = context['data']['footer_links'].get(link, {}).copy()
        footer_links.append(link_data)
    context['data']['footer_links'] = footer_links

    return context

def html_page_context_listener(app, pagename, templatename, context, doctree):
    """Add site data to Sphinx context, to make porting templates easier"""
    context['site'] = app.site_data
    # The translation context is pinned to the Italian sources, as Sphinx has
    # it's own translation mechanism built in
    if 'language' in context:
        language = context['language']
    else:
        language = app.site_data['default_language']
    context['t'] = app.site_data['data']['l10n'][language]['t']

def setup(app):
    app.site_data = load_site_data()
    app.connect('html-page-context', html_page_context_listener)
