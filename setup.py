"""Distutils script for dicto.

To install:
    python setup.py install

"""

import sys

from distutils.core import setup

modules = [
        "dicto",
]

setup(
        name = "dicto",
        version = "0.1.0",
        description = "dict subclass to allow dotted notation",
        license = "Python Software Foundation License",
        long_description = "dict subclass to allow dotted notation",
        author = "Evan Burt",
        author_email = "kurohai@gmail.com",
        maintainer = "Evan Burt",
        maintainer_email = "kurohai@gmail.com",
        url = "http://github.com/kurohai/dicto",
        py_modules = modules,
        # packages = ["ceGUI"],
        # scripts = ["img2py.py"],
)

