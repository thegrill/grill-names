#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# grill.names documentation build configuration file, created by
# sphinx-quickstart on Sun Apr  9 21:39:36 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
# namingpath = r'B:\write\code\git\naming'
# grillnamespath = r'B:\write\code\git\grill-names'
# import sys
# sys.path.append(namingpath)
# sys.path.append(grillnamespath)

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              # 'sphinx.ext.imgmath',
              # 'sphinx.ext.ifconfig',
              'sphinx.ext.viewcode',
              'sphinx.ext.graphviz',
              'sphinx.ext.inheritance_diagram',
              'sphinx.ext.autosectionlabel',
              'sphinx_copybutton',
              'sphinx_toggleprompt',
              'sphinx_togglebutton',
              'm2r2',
              'hoverxref.extension',
              'sphinx_autodoc_typehints']

# Offset to play well with copybutton
toggleprompt_offset_right = 35

togglebutton_hint = " "
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'naming': ('http://naming.readthedocs.io/en/latest/', None),
}
# ----- hoverxref -----
hoverxref_auto_ref = True
hoverxref_intersphinx = [
  'naming',
]
hoverxref_intersphinx_types = dict.fromkeys(intersphinx_mapping, 'tooltip')
hoverxref_domains = ['py']

# ----- sphinx-autodoc-typehints -----
always_document_param_types = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# graphviz_dot = r'B:\__appdata__\graphviz\bin\dot.exe'
# inheritance_graph_attrs = dict(rankdir="LR", size='"6.0, 8.0"',fontsize=14, ratio='compress')
inheritance_graph_attrs = dict(rankdir="TB", bgcolor='transparent')

# inheritance_node_attrs = dict(shape='Mrecord', fontsize=14, height=0.75, color='dodgerblue1', style='filled')
inheritance_node_attrs = dict(shape='Mrecord', color='"#2573a7"', style='filled', fillcolor='"#eaf4fa"',
                              size='"6.0, 8.0"')

inheritance_edge_attrs = dict(color='"#123a54"')

autodoc_member_order = 'groupwise'
autodoc_default_flags = ['members', 'show-inheritance']

graphviz_output_format = 'svg'
# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'grill.names'
copyright = '2017, The Grill'
author = 'Christian López Barrón'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '2.5'
# The full version, including alpha/beta/rc tags.
release = '2.5.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'
highlight_language = 'python3'
# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'grillnamesdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}


# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'grillnames.tex', 'grill.names Documentation',
     'The Grill', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'grillnames', 'grill.names Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'grillnames', 'grill.names Documentation',
     author, 'grillnames', 'One line description of project.',
     'Miscellaneous'),
]

