#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Metplotlib

Import tests
"""
import metplotlib
from metplotlib import colormaps
from metplotlib import plots
from metplotlib import PACKAGE_ROOTDIR

tcl = colormaps.temperature_colorlevels
plots.twovar_comparison

print(f"Package {metplotlib.__name__}-v{metplotlib.__version__} successfully imported from {PACKAGE_ROOTDIR}")
