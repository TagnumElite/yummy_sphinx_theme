niftools_sphinx_theme
=====================

.. toctree::
   :maxdepth: 1

Configuration
=============

Navagation
----------
* ``home``: :py:class:`str`. `URL to home page`
* ``projects``: :py:class:`str`. `URL to projects page`
* ``blog``: :py:class:`str`. `URL to blog page`
* ``forums``: :py:class:`str`. `URL to forums`
* ``about``: :py:class:`str`. `URL to about page`

.. note::
    If you don't specify home it's link will be replaced with the docs root.
    
    It will prefer the page `about` rather than the url.

Social
------
* ``twitter``: :py:class:`str`. `Twitter account name`
* ``discord_id``: :py:class:`int`. `Discord Server/Guild ID`
* ``discord_invite``: :py:class:`str`. `Discord Server/Guild Invite Url`
* ``youtube``: :py:class:`str`. `YouTube Channel Name`

Badges
------
* ``badges``: :py:class:`bool`. `Enable/Disable Badges. Defaults to False`
* ``travis``: :py:class:`str`. `USER/REPO/BRANCH`
* ``appveyor``: :py:class:`str`. `USER/REPO/BRANCH`
* ``jenkins``: :py:class:`str`. `URL to travis` Not quite tested
* ``coveralls``: :py:class:`str`. `USER/REPO/BRANCH`
* ``github``: :py:class:`str`. `USER/REPO`
* ``pypi``: :py:class:`str`. `PROJECT`
* ``rtd``: :py:class:`str`. `PROJECT`

Tracking
--------
* ``analytics``: :py:class:`str`. `Google Analytics Code`

Example
-------

.. code:: python

    html_theme_options = {
        'home': 'http://example.com',
        'projects': 'http://projects.example.com',
        'blog': 'http://blog.example.com',
        'forums': 'http://forum.example.com',
        'about': 'http://example.com/about',
        'twitter': 'TagnumElite', #https://twitter.com/TagnumElite
        'discord_id': 179892881627021312,
        'discord_invite': 'https://discord.gg/5YWnJKu',
        'youtube': 'UChphbk4d1OvPilYwRnj_Z5w', #https://www.youtube.com/channel/UChphbk4d1OvPilYwRnj_Z5w
        'badges': True,
        'travis': 'TagnumElite/niftools_sphinx_theme', #https://travis-ci.org/TagnumElite/niftools_sphinx_theme
        'appveyor': 'gruntjs/grunt', #https://ci.appveyor.com/project/gruntjs/grunt/
        'coveralls': 'jekyll/jekyll', #https://codeclimate.com/github/jekyll/jekyll/
        'github': 'TagnumElite/niftools_sphinx_theme', #https://github.com/TagnumElite/niftools_sphinx_theme
        'pypi': 'niftools-sphinx-theme', #https://pypi.org/project/niftools-sphinx-theme/
        'rtd': 'vectorbot' #http://vectorbot.readthedocs.io
    }

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
