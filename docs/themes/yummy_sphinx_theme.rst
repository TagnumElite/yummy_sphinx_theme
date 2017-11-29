yummy_sphinx_theme
==================

.. toctree::
   :maxdepth: 1

Configuration
-------------

Navagation
^^^^^^^^^^
* ``navs``: :py:class:`dict`. `A dictionary of nav links`

.. note::
    If you leave navs alone it will create a link with you projects
    name on their to the home page.

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

Tracking
^^^^^^^^
* ``google_tracking_id``: :py:class:`str`. `Google Analytics Code`

Colors
^^^^^^
* ``navbar_base_color``: :py:class:`str`. ` `HTML Color code <https://www.w3schools.com/colors/default.asp>`_ `

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
        'gitlab_url': 'TagnumElite/yummy_sphinx_theme'
    }

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
