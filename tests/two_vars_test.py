#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Metplotlib

Testing of the two-variable plots on fake data.
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
mslp_r = mslp + np.random.rand(*mslp.shape)
t2m_r = t2m + np.random.rand(*t2m.shape)


def test_twovar_plot():
    fig, ax = plots.twovar_plot(
        mslp, t2m, lons=lon, lats=lat, cl_varfamily="temp", resolution="110m"
    )
    fig.show()
    assert fig and ax


def test_twovar_comparison():
    fig, ax = plots.twovar_comparison(
        mslp,
        mslp_r,
        t2m,
        t2m_r,
        lons=lon,
        lats=lat,
        cl_varfamily="temp",
        resolution="110m",
    )
    fig.show()
    assert fig and ax.all()


if __name__ == "__main__":
    test_twovar_plot()
    test_twovar_comparison()
