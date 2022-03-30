##############
### Settings
#############


PROJECT = "{{cookiecutter.project_name}}"  # !!! Suppose that github repo has the same name as python folder with main files
AUTHOR = "{{cookiecutter.author}}"  # Change it to your values
GITHUB_USER = "{{cookiecutter.github_user}}"  # Change it to your values

# Template suppose separate build and source structure


#####################
### End of settings
####################

# No need of editting further


import sys
import pathlib
import datetime


# Folders to sys path to be able to import
script_dir = pathlib.Path(__file__).resolve()
root = script_dir.parents[2]
lib_path = root / PROJECT

for i in [script_dir, root, lib_path]:
    if i.as_posix() not in sys.path:
        sys.path.insert(0, i.as_posix())

# -- Project information -----------------------------------------------------

copyright = f"2020, {AUTHOR}"  # pylint: disable=redefined-builtin

# The full version, including alpha/beta/rc tags
release = datetime.datetime.now().strftime("%d-%m-%Y")

master_doc = "index"  # pylint: disable=invalid-name

source_suffix = [".rst", ".md"]

# -- General configuration ---------------------------------------------------
html_theme_options = {
    "github_user": GITHUB_USER,
    "github_repo": PROJECT,
    "github_banner": True,
}


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    # "sphinx.ext.imgmath",
    # "sphinx.ext.autosectionlabel",
    # "m2r2",
]

# 'about.html',
html_sidebars = {"**": ["navi.html", "searchbox.html"]}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"  # pylint: disable=invalid-name

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# html_extra_path = ['../extra']

html_css_files = [
    "https://malachov.github.io/readthedocs-sphinx-alabaster-css/custom.css",
]

# napoleon_custom_sections = [
#     ("Types", "returns_style"),
#     ("Type", "returns_style"),
#     ("Options", "returns_style"),
#     ("Default", "returns_style"),
#     ("Example", "returns_style"),
#     ("Examples", "returns_style"),
# ]
