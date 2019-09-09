==================
Yummy Sphinx Theme
==================

.. image:: https://img.shields.io/pypi/v/yummy_sphinx_theme.svg
    :target: https://pypi.org/project/yummy_sphinx_theme/

.. image:: https://img.shields.io/github/release/TagnumElite/yummy_sphinx_theme/all.svg
    :target: https://github.com/TagnumElite/yummy_sphinx_theme

.. image:: https://img.shields.io/pypi/l/yummy_sphinx_theme.svg
    :target: https://pypi.org/project/yummy_sphinx_theme/

.. image:: https://img.shields.io/pypi/pyversions/yummy_sphinx_theme.svg
    :target: https://pypi.org/project/yummy_sphinx_theme/

.. image:: https://img.shields.io/github/issues-raw/TagnumElite/yummy_sphinx_theme.svg
    :target: https://github.com/TagnumElite/yummy_sphinx_theme

.. image:: https://img.shields.io/travis/TagnumElite/yummy_sphinx_theme/develop.svg
    :target: https://travis-ci.org/TagnumElite/yummy_sphinx_theme

The yummy_sphinx_theme is created from `DONGChuan's Yummy-Jekyll <https://github.com/DONGChuan/Yummy-Jekyll>`_

.. contents::

`Demo <http://tagnumelite.com/yummy_sphinx_theme>`_
===================================================

Installation
============
There are two ways to install these themes

Via Python Package Interface
----------------------------

Download the package and add ``sphinx`` to your ``requirements.txt`` file:

.. code:: bash

    pip install yummy_sphinx_theme

In your ``conf.py`` file:

.. code:: python

    html_theme = "yummy_sphinx_theme"

Via git or download
-------------------

Download the ``yummy_sphinx_theme`` folder into your documentation at
``docs/_themes/`` then add the following two lines to your Sphinx
``conf.py`` file:

.. code:: python

    html_theme = "yummy_sphinx_theme"
    html_theme_path = ["_themes", ]
