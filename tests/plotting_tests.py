#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Metplotlib

Plotting tests
"""

import numpy as np

from metplotlib import plots

nx, ny = (245, 265)
lon, lat = np.meshgrid(
    np.linspace(-20, 3, nx),
    np.linspace(45, 60, ny),
)
t2m = 30 * np.cos(np.pi * lat / 180) + np.sin(20 * np.pi * lon / 180)
mslp = 1015 + 10 * (np.sin(20 * np.pi * lon / 180) + np.cos(25 * np.pi * lat / 180))

fig, ax = plots.twovar_plot(mslp, t2m, lons=lon, lats=lat, cl_varfamily="temp")
fig.show()
