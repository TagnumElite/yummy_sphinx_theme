# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
from os.path import dirname, abspath, join
import sys
sys.path.insert(0, dirname(dirname(abspath(__file__))))


# -- Project information -----------------------------------------------------

project = 'Yummy Sphinx Theme'
copyright = '2019, TagnumElite'
author = 'TagnumElite'

# The full version, including alpha/beta/rc tags
from yummy_sphinx_theme import __version__
release = __version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'yummy_sphinx_theme'
html_theme_path = [join(dirname(dirname(__file__)))]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'navs': {
        'Home': 'http://tagnumelite.elitekast.com'
    },
    'github_url': 'TagnumElite/yummy_sphinx_theme',
    'google_tracking_id': 'UA-49499868-10',
    'disqus': 'yummysphinxtheme',
    'canonical_url': "http://tagnumelite.elitekast.com/yummy_sphinx_theme",
    'navbar_icon': 'spin fa-book',
}

html_logo = '_static/favicon.ico'
