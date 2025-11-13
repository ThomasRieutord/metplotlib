#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Metplotlib

Testing of the single-variable plots on fake data.
"""

import cartopy.crs as ccrs
import numpy as np
import matplotlib.pyplot as plt

from metplotlib import plots

nx, ny = (245, 265)
lon, lat = np.meshgrid(
    np.linspace(-20, 3, nx),
    np.linspace(45, 60, ny),
)
t2m = 30 * np.cos(np.pi * lat / 180) + np.sin(20 * np.pi * lon / 180)
mslp = 1015 + 10 * (np.sin(20 * np.pi * lon / 180) + np.cos(25 * np.pi * lat / 180))

# Data CRS: how the data is stored
data_crs = ccrs.PlateCarree()
# Figure CRS: what the figure will look like
fig_crs = ccrs.Orthographic(central_latitude=45, central_longitude=0)


def set_fig_ax():
    fig = plt.figure(figsize=plots.DEFAULT_FIGSIZE)
    ax = plt.subplot(projection=fig_crs)
    ax.coastlines(resolution="110m", color="black", linewidth=0.5)
    return fig, ax


def test_isolines():
    FIG, AX = set_fig_ax()
    fig, ax = plots.isolines(mslp, lons=lon, lats=lat, fig=FIG, ax=AX, datcrs=data_crs)
    fig.show()
    assert fig and ax


def test_colorlevels():
    FIG, AX = set_fig_ax()
    fig, ax = plots.colorlevels(
        t2m, lons=lon, lats=lat, fig=FIG, ax=AX, datcrs=data_crs
    )
    fig.show()
    assert fig and ax


def test_colorshades():
    FIG, AX = set_fig_ax()
    fig, ax = plots.colorshades(
        t2m, lons=lon, lats=lat, fig=FIG, ax=AX, datcrs=data_crs
    )
    fig.show()
    assert fig and ax


def test_scatter():
    lon = -20 + (50 + 20) * np.random.rand(500)
    lat = 30 + (70 - 30) * np.random.rand(500)
    data = 20 + 5 * (np.cos(np.deg2rad(lat) * 4) + np.sin(np.deg2rad(lon) * 4))
    fig, ax = plots.scatter(data, lon, lat, varfamily="temperature")
    fig.show()
    assert fig and ax


if __name__ == "__main__":
    test_isolines()
    test_colorlevels()
    test_colorshades()
    test_scatter()
