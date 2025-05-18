# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
import os
import datetime

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Yuheng"
copyright = f"{datetime.datetime.now().year}, OSMChina"
author = "OSMChina"

# Try to get version from const.py
try:
    from src.yuheng.basic.const import YUHENG_VERSION
    version = YUHENG_VERSION
    release = YUHENG_VERSION
except ImportError:
    version = "1.4.0"
    release = "1.4.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.githubpages',
    'sphinx_autodoc_typehints',
    'sphinx_copybutton',
    'myst_parser',
]

# Configure myst-parser to handle Markdown files
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]

# Theme options
html_theme_options = {
    "sidebar_hide_name": False,
    "light_css_variables": {
        "color-brand-primary": "#336699",
        "color-brand-content": "#336699",
    },
    "dark_css_variables": {
        "color-brand-primary": "#6699cc",
        "color-brand-content": "#6699cc",
    },
}

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'requests': ('https://requests.readthedocs.io/en/latest/', None),
}
