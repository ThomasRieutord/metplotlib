#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Metplotlib

https://github.com/ThomasRieutord/metplotlib
"""
from pathlib import Path
import importlib.metadata

package_rootdir = str(Path(__file__).parent.parent.resolve())

__version__ = importlib.metadata.version("metplotlib")

__all__ = ["package_rootdir", "__version__"]
