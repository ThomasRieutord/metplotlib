#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Metplotlib

Colormap loading

Color levels -> ListedColormap (discrete set of values), used in `matplotlib.pyplot.contourf`
Color maps -> Colormap (continuous set of values), used in `matplotlib.pyplot.pcolormesh`
"""
import json
import os

import numpy as np
from matplotlib import colors

from metplotlib import PACKAGE_ROOTDIR


def _load_colormap_from_json(jsonfile):
    """Load the colormap written in a JSON file


    Parameters
    ----------
    jsonfile: str
        Path to the JSON file to be written


    Returns
    -------
    colormap: `matplotlib.colors.ListedColormap`
        The colormap

    norm: `matplotlib.colors.BoundaryNorm`
        The boundaries of the color levels
    """
    with open(jsonfile, "r") as jsf:
        temp_colors = json.load(jsf)

    norm = colors.BoundaryNorm(temp_colors["bounds"], temp_colors["N"])
    colormap = colors.ListedColormap(temp_colors["colors"], name=temp_colors["name"])

    return colormap, norm


# Color levels -> ListedColormap (discrete set of values), used in `matplotlib.pyplot.contourf`
# ------------
temperature_colorlevels = _load_colormap_from_json(
    os.path.join(
        PACKAGE_ROOTDIR, "metplotlib", "colormaps", "temperature_colorlevels.json"
    )
)
radar_colorlevels = _load_colormap_from_json(
    os.path.join(PACKAGE_ROOTDIR, "metplotlib", "colormaps", "radar_colorlevels.json")
)
wind_colorlevels = _load_colormap_from_json(
    os.path.join(PACKAGE_ROOTDIR, "metplotlib", "colormaps", "wind_colorlevels.json")
)

def get_colorlevels_from_varfamily(varfamily):
    """Return the color levels (discrete set of color values) corresponding to the variable family


    Parameters
    ----------
    varfamily: str
        Variable family (ex: "temperature", "radar", "wind_speed")


    Returns
    -------
    colorlevels: tuple of (`ListedColormap`, `BoundaryNorm`)
        Discrete values colormap and boundaries for the color to be applied
    """
    if varfamily in ["T", "temp", "temperature"] or varfamily[:15] == "air_temperature":
        colorlevels = temperature_colorlevels
    elif varfamily in ["FF", "wind", "wind_speed"]:
        colorlevels = wind_colorlevels
    elif varfamily in ["RR", "radar", "precipitation"]:
        colorlevels = radar_colorlevels
    else:
        raise ValueError(f"Unable to find color levels for varfamily={varfamily}")

    return colorlevels


# Color maps -> Colormap (continuous set of values), used in `matplotlib.pyplot.pcolormesh`
# ----------
temperature_colormap = "rainbow"
wind_colormap = "spring"
diff_colormap = "bwr"
default_colormap = "viridis"


def get_colormap_from_varfamily(varfamily):
    """Return the colormap (continuous set of color values) corresponding to the variable family


    Parameters
    ----------
    varfamily: str
        Variable family (ex: "temperature", "radar", "wind_speed")


    Returns
    -------
    colorshade: str
        Name of the matplotlib colormap for this family of variable
    """
    if varfamily in ["T", "temp", "temperature"] or varfamily[:15] == "air_temperature":
        colorshade = temperature_colormap
    elif varfamily in ["FF", "wind", "wind_speed"]:
        colorshade = wind_colormap
    elif varfamily.lower() == "diff":
        colorshade = diff_colormap
    else:
        colorshade = default_colormap

    return colorshade


# Remove unnecessary attributes
del json, np, colors, os, PACKAGE_ROOTDIR
