#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Metplotlib

Import tests
"""

import metplotlib
from metplotlib import colormaps
from metplotlib import plots
from metplotlib import PACKAGE_ROOTDIR


def test_imports():
    tcl = colormaps.TEMPERATURE_COLORLEVELS
    print(
        f"Package {metplotlib.__name__}-v{metplotlib.__version__} successfully imported from {PACKAGE_ROOTDIR}"
    )
    assert tcl and plots.twovar_comparison


if __name__ == "__main__":
    test_imports()
