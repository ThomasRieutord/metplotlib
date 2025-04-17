#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Metplotlib

https://github.com/ThomasRieutord/metplotlib
"""
from pathlib import Path
import importlib.metadata

PACKAGE_ROOTDIR = str(Path(__file__).parent.parent.resolve())

__version__ = importlib.metadata.version("metplotlib")

__all__ = ["PACKAGE_ROOTDIR", "__version__"]
