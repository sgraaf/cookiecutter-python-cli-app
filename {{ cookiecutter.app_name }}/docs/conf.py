"""Sphinx configuration."""

from importlib import metadata
from typing import Any

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "{{ cookiecutter.friendly_name }}"
copyright = "{{ cookiecutter.copyright_year }}, {{ cookiecutter.author }}"
author = "{{ cookiecutter.author }}"
release = metadata.version("{{ cookiecutter.package_name }}")
version = release.rsplit(".", 1)[0]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autodoc.typehints",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
    "sphinxext.opengraph",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# auto-generate header anchors and suppress header warnings
myst_heading_anchors = 3
suppress_warnings = ["myst.header"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# move type hints into the description block, instead of the signature
autodoc_typehints = "description"
autodoc_typehints_description_target = "documented"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]
html_theme_options: dict[str, Any] = {
    "top_of_page_buttons": [],
}
