'''
Author: qufeng107 qufeng107@gmail.com
Date: 2024-04-06 15:53:16
LastEditors: qufeng107 qufeng107@gmail.com
LastEditTime: 2024-04-06 23:44:32
FilePath: \OxValueAIDoc\docs\source\conf.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'OxValueAI'
copyright = '2024, OxValueAI'
author = 'Feng'

release = '0.1'
version = '0.1.0'
language = 'en'

locale_dirs = ['../locales/']   # path is example but recommended.
gettext_compact = False  # optional.
gettext_uuid = True  # optional.

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'


# import custom css files
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]
