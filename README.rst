.. _demo: http://tagnumelite.elitekast.com/yummy_sphinx_theme

*********************
Yummy Sphinx Theme
*********************

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
    :target: https://travis-ci.org/niftools/TagnumElite/yummy_sphinx_theme

.. contents::

Demo_
=====

Installation
============
There are two ways to install this theme

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
``docs/_themes/`` then add the following two settings to your Sphinx
``conf.py`` file:

.. code:: python

    html_theme = "yummy_sphinx_theme"
    html_theme_path = ["_themes", ]

Configuration
=============

The theme's project-wide options are defined in the ``yummy_sphinx_theme/theme.conf``
file of this repository, and can be defined in your project's ``conf.py`` via
``html_theme_options``.

For example:

.. code:: python

    html_theme_options = {
        'home': 'https://github.com/TagnumElite',
        'projects': 'https://github.com/TagnumElite/?tab=repositories',
        'blog': 'https://tagnumelite.elitekast.com',
        'forums': 'https://forums.example.com'
    }

If `home` is not specified in the theme_options it turns into the documentation home.
If `home` is specified then there is a new option called Documentation on the navbar.

.. include:: CHANGELOG.rst