# -*- coding: utf-8 -*-
"""
Copyright (c) François Pinot, May 2016
"""

import notebook
import os.path
import site
import shutil

# Copy csoundmagics in user site-packages dir
dest = site.getusersitepackages()
shutil.copy("csoundmagics.py", dest)

# Copy csound mode in codemirror
dest = os.path.join(notebook.DEFAULT_STATIC_FILES_PATH, "components", "codemirror", "mode", "csound")
if not os.path.exists(dest):
    os.mkdir(dest)
shutil.copy("csound.js", dest)

# Copy custom.js in jupyter dir
dest = os.path.join(notebook.extensions.jupyter_config_dir(), "custom")
if not os.path.exists(dest):
    os.mkdir(dest)
shutil.copy("custom.js", dest)
