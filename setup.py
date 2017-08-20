#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='grill-names',
    version='1.0.0',
    packages=find_packages(
        exclude=("*.tests", "*.tests.*", "tests.*", "tests", "*.docs", "*.docs.*", "docs.*", "docs")),
    description='Name objects for digital content creation.',
    author='Christian López Barrón',
    author_email='chris.gfz@gmail.com',
    url='https://github.com/thegrill/grill-names',
    download_url='https://github.com/thegrill/grill-names/releases/tag/1.0.0',
    classifiers=['Programming Language :: Python :: 3.6'],
    extras_require={'docs': ['sphinx_autodoc_typehints', 'sphinx_rtd_theme']},
    install_requires=['naming'],
    namespace_packages=['grill']
)
