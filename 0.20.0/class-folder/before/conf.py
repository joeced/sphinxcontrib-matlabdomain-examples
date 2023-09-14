import os
import sphinx_rtd_theme

matlab_src_dir = os.path.abspath(os.path.join("..", "matlab-files"))
matlab_short_links = True
extensions = ["sphinx.ext.autodoc", "sphinxcontrib.matlab", "sphinx_rtd_theme"]
primary_domain = "mat"
project = "Class folder example"
master_doc = "index"
source_suffix = ".rst"
nitpicky = True
html_theme = "sphinx_rtd_theme"
