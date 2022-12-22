# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ActKing'
copyright = '2022, HikaruSatomura'
author = 'HikaruSatomura'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys
sys.path.insert(0, os.path.abspath('../Script/System'))
sys.path.insert(0, os.path.abspath('../Script/System/Game'))
sys.path.insert(0, os.path.abspath('../Script/System/Game/Battle'))
sys.path.insert(0, os.path.abspath('../Script/System/Game/Data'))
sys.path.insert(0, os.path.abspath('../Script/System/Game/Title'))
sys.path.insert(0, os.path.abspath('../Script/System/IO'))
sys.path.insert(0, os.path.abspath('../Script/System/Util'))
sys.path.insert(0, os.path.abspath('../Script/System/Util/Command'))


extensions = ["sphinx.ext.autodoc","sphinx.ext.autosummary"]

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinxjp'
