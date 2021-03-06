from io import open
from setuptools import setup
from yummy_sphinx_theme import __version__

setup(
    name='yummy_sphinx_theme',
    version=__version__,
    description='A sphinx theme created to mirror Yummy-Jekyll',
    long_description=open('README.rst', encoding='utf-8').read(),
    author='Tagan Hoyle',
    author_email='tagnum.elite@gmail.com',
    url='https://github.com/TagnumElite/yummy_sphinx_theme',
    license='MIT',
    packages=['yummy_sphinx_theme'],
    include_package_data=True,
    package_data={
        'yummy_sphinx_theme': [
            'theme.conf',
            '*.html',
            'static/css/*.css',
            'static/js/*.js',
            'static/fonts/*.*'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points= {
        'sphinx.html_themes': [
            'yummy_sphinx_theme = yummy_sphinx_theme'
        ]
    }
)
