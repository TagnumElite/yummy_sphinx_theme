.. niftools_sphinx_theme documentation master file, created by
   sphinx-quickstart on Tue Sep 12 07:25:47 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Yummy Sphinx Theme documentation!
============================================

.. toctree::
   :maxdepth: 1

Configuration
-------------

Navagation
^^^^^^^^^^
* ``navs``: :py:class:`dict`. `A dictionary of nav links`
* ``navbar_icon``: :py:class:`str`. ` `A font-awesone icon <http://fontawesome.io/icons/>`_ `
* ``home_name``: :py:class:`str`. `String use to customise home nav key. Default: (Documentation)`

.. note::
    If you leave navs alone it will create a link with your project's
    name on their to the home page.

Custom Styles
^^^^^^^^^^^^^
* ``font_awesome_embed_code``: :py:class:`str`. `A font-awesome embed code (0cb92b034c.js)`

TOC Tree
^^^^^^^^
* ``toc_depth``: :py:class:`int`. `Depth of TOC tree`
* ``toc_collapse``: :py:class:`bool`. `Collapse TOC Tree`
* ``toc_hidden``: :py:class:`bool`. `Include hidden`

Urls
^^^^
* ``canonical_url``: :py:class:`str`. `Canonical Url`
* ``github_url``: :py:class:`str`. `Username/Repository`
* ``bitbucket_url``: :py:class:`str`. `Username/Repository`
* ``gitlab_url``: :py:class:`str`. `Username/Repository`
* ``disqus``: :py:class:`str`. `Full Disqus Url`

.. note::
    ``github_url``, ``bitbucket_url`` or ``gitlab_url`` will result
    in a each respective icon in the footer.

Analytics
^^^^^^^^^
* ``google_tracking_id``: :py:class:`str`. `Google Analytics Code`

Colors
^^^^^^
* Navbar
    * ``navbar_bg_color``: :py:class:`str`. `HTML color code`_
    * ``navbar_text_color``: :py:class:`str`. `HTML color code`_
    * ``navbar_brand_color``: :py:class:`str`. `HTML color code`_
    * ``navbar_hover_color``: :py:class:`str`. `HTML color code`_
* Jumbotron
    * ``jumbotron_text_color``: :py:class:`str`. `HTML color code`_
    * ``jumbotron_link_color``: :py:class:`str`. `HTML color code`_
* Footer
    * ``footer_text_color``: :py:class:`str`. `HTML color code`_
    * ``footer_icon_color``: :py:class:`str`. `HTML color code`_
    * ``footer_icon_hover_color``: :py:class:`str`. `HTML color code`_
* TOC
    * ``toc_bg_color``: :py:class:`str`. `HTML color code`_
    * ``toc_text_color``: :py:class:`str`. `HTML color code`_
    * ``toc_hover_color``: :py:class:`str`. `HTML color code`_

Example
^^^^^^^

.. code:: python

    html_theme_options = {
        'navs': '{
            'Home': 'http://tagnumelite.elitekast.com',
            'Blog': 'http://blog.elitekast.com',
            'Forum': 'http://forum.elitekast.com',
        },
        'github_url': 'TagnumElite/yummy_sphinx_theme',
        'bitbucket_url': 'TagnumElite/yummy_sphinx_theme',
        'gitlab_url': 'TagnumElite/yummy_sphinx_theme',
        'navbar_icon': 'spin fa-book'
    }

.. _HTML color code: https://www.w3schools.com/colors/default.asp

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
