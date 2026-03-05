"""Sphinx configuration for the orbitals documentation."""

from __future__ import annotations

import os
import sys
from datetime import date

sys.path.insert(0, os.path.abspath("../src"))

project = "Orbitals"
copyright = f"{date.today().year}, Orbitals contributors"
author = "Orbitals contributors"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

autodoc_member_order = "bysource"
html_theme = "sphinx_rtd_theme"
