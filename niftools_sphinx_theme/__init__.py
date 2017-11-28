"""
NifTools Sphinx Theme, created to mimick the niftools.org website
"""
from os import path

__version__ = '0.0.7'

def get_path():
    """Return list of HTML theme paths."""
    return path.abspath(path.dirname(path.dirname(__file__)))

def setup(app):
    app.add_html_theme('niftools_sphinx_theme', path.abspath(path.dirname(__file__)))
    return {'version': __version__}
