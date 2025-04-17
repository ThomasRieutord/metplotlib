#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Metplotlib

Colormap loading

Color levels -> ListedColormap (discrete set of values), used in `matplotlib.pyplot.contourf`
Color maps -> Colormap (continuous set of values), used in `matplotlib.pyplot.pcolormesh`
"""

from matplotlib import colors
from .dicts import (
    TEMPERATURE_COLORLEVELS_DICT,
    RADAR_COLORLEVELS_DICT,
    WIND_COLORLEVELS_DICT,
)

__all__ = [
    "get_colorlevels_from_varfamily",
    "get_colormap_from_varfamily",
    "TEMPERATURE_COLORLEVELS",
    "RADAR_COLORLEVELS",
    "WIND_COLORLEVELS",
    "TEMPERATURE_COLORMAP",
    "WIND_COLORMAP",
    "DIFF_COLORMAP",
    "DEFAULT_COLORMAP",
]


def _load_colormap_from_dict(colordict):
    """Load the colormap written in a JSON file


    Parameters
    ----------
    colordict: dict
        Path to the JSON file to be written


    Returns
    -------
    colormap: `matplotlib.colors.ListedColormap`
        The colormap

    norm: `matplotlib.colors.BoundaryNorm`
        The boundaries of the color levels
    """
    norm = colors.BoundaryNorm(colordict["bounds"], colordict["N"])
    colormap = colors.ListedColormap(colordict["colors"], name=colordict["name"])

    return colormap, norm


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
        colorlevels = TEMPERATURE_COLORLEVELS
    elif varfamily in ["FF", "wind", "wind_speed"]:
        colorlevels = WIND_COLORLEVELS
    elif varfamily in ["RR", "radar", "precipitation"]:
        colorlevels = RADAR_COLORLEVELS
    else:
        raise ValueError(f"Unable to find color levels for varfamily={varfamily}")

    return colorlevels


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
        colorshade = TEMPERATURE_COLORMAP
    elif varfamily in ["FF", "wind", "wind_speed"]:
        colorshade = WIND_COLORMAP
    elif varfamily.lower() == "diff":
        colorshade = DIFF_COLORMAP
    else:
        colorshade = DEFAULT_COLORMAP

    return colorshade


# Color levels -> ListedColormap (discrete set of values), used in `matplotlib.pyplot.contourf`
# ------------
TEMPERATURE_COLORLEVELS = _load_colormap_from_dict(TEMPERATURE_COLORLEVELS_DICT)
RADAR_COLORLEVELS = _load_colormap_from_dict(RADAR_COLORLEVELS_DICT)
WIND_COLORLEVELS = _load_colormap_from_dict(WIND_COLORLEVELS_DICT)


# Color maps -> Colormap (continuous set of values), used in `matplotlib.pyplot.pcolormesh`
# ----------
TEMPERATURE_COLORMAP = "rainbow"
WIND_COLORMAP = "spring"
DIFF_COLORMAP = "bwr"
DEFAULT_COLORMAP = "viridis"
