"""Sphinx configuration."""
project = "Pluggable Apps with Antidote"
html_title = "Pluggable Apps with Antidote"
author = "Paul Everitt"
copyright = "2022, Paul Everitt"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
    "sphinx.ext.intersphinx",
]
autodoc_typehints = "description"
html_theme = "furo"
intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
    "antidote": ("https://antidote.readthedocs.io/en/stable/", None),
    "pyramid": ("https://docs.pylonsproject.org/projects/pyramid/en/latest", None),
}
myst_url_schemes = ["http", "https", "mailto"]
myst_enable_extensions = ["colon_fence"]
