import os
import sphinx_rtd_theme

matlab_src_dir = os.path.abspath(os.path.join("..", "matlab-files"))
matlab_short_links = True
matlab_auto_link = "all"
extensions = ["sphinx.ext.autodoc", "sphinxcontrib.matlab", "sphinx_rtd_theme"]
primary_domain = "mat"
project = "test_autodoc"
master_doc = "index"
source_suffix = ".rst"
nitpicky = True
html_theme = "sphinx_rtd_theme"
