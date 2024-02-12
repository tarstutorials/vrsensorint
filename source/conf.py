# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'VRSensorIntegration'
copyright = '2024, Ethan Matzek, Tyler Yankee, Odin Kohler, Maryangela White, Matt Duver, Robert Licata, Niall Pepper, Sean Banerjee, Natasha Kholgade Banerjee'
author = 'Ethan Matzek, Tyler Yankee, Odin Kohler, Maryangela White, Matt Duver, Robert Licata, Niall Pepper, Sean Banerjee, Natasha Kholgade Banerjee'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autosectionlabel', 'sphinx_rtd_theme', 'sphinxcontrib.quizdown']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# NOTE: WE ARE USING THE READTHEDOCS THEME. IF YOU DON'T HAVE IT INSTALLED, FOLLOW THE INSTRUCTIONS IN THIS VIDEO: https://www.youtube.com/watch?v=Zb_Oy5UG6Tw&ab_channel=CodeWithRajRanjan.
#MAKE SURE TO INSTALL THE THEME IN THE /DOCS SUBFOLDER.
#IF YOU DONT WANT TO INSTALL IT BUT STILL WANT TO BUILD THE WEBSITE, COMMENT THE LINE BELOW AND UNCOMMENT THE LINE BELOW THAT TO USE A DEFAULT THEME. 
html_theme = "sphinx_rtd_theme"
#html_theme = "alabaster"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
#Change the logo that appears on the website. Must be in same directory as conf.py file.
html_logo = 'images/tars_logo.jpeg'
# Options to change the HTML output for the site. Specific to the theme.
html_theme_options = {
    
}
