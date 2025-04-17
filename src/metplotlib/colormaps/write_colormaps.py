#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Metplotlib

Write colormap from various source of information
"""

import json
import os

import numpy as np
from matplotlib import colors

# Define the colormaps from various sources
# -----------------------------------------

# From T. Kokina
wind_colors = np.array(
    [
        colors.to_rgb(c)
        for c in [
            "white",
            "lightblue",
            "lightsteelblue",
            "cornflowerblue",
            "royalblue",
            "yellowgreen",
            "limegreen",
            "yellow",
            "orange",
            "red",
            "brown",
            "black",
        ]
    ]
)
wind_colormap = colors.ListedColormap(wind_colors)
wind_values = np.array([0, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 300])
wind_norm = colors.BoundaryNorm(wind_values, wind_colormap.N)

# From R. Darcy
radar_bounds = [0, 0.1, 0.5, 1, 2.5, 5, 10, 25, 50, 100, 200]
radar_values = [0, 0.1, 0.5, 1, 2.5, 5, 10, 25, 50, 100]
radar_colormap = colors.ListedColormap(
    [
        (1, 1, 1),
        (1, 0.6392156863, 0.2039215686),
        (0.4549019608, 1, 0.3058823529),
        (0, 0.8039215686, 0.2392156863),
        (0, 1, 0.9960784313),
        (0.5215686275, 0.8117647059, 0.9098039216),
        (0.1176470588, 0.0862745098, 0.9647058824),
        (0.9450980392, 0.5058823529, 0.9098039216),
        (0.8274509804, 0.0901960784, 0.5490196078),
        (0.6, 0.6, 0.6),
    ]
)
radar_colormap = radar_colormap(np.arange(radar_colormap.N))
radar_colormap[0, 3] = 0
radar_colormap = colors.ListedColormap(radar_colormap)
radar_norm = colors.BoundaryNorm(radar_bounds, radar_colormap.N)

# From R. Darcy
temp_bounds = np.arange(-32, 44, 2)
temp_values = np.arange(-30, 42, 2)
ecmwf_temp_rgb = [
    [76, 76, 76],
    [102, 102, 102],
    [128, 128, 128],
    [153, 153, 153],
    [179, 179, 179],
    [204, 204, 204],
    [89, 0, 153],
    [128, 0, 230],
    [153, 51, 255],
    [191, 102, 255],
    [217, 153, 255],
    [0, 0, 191],
    [0, 0, 255],
    [51, 102, 255],
    [102, 179, 255],
    [153, 230, 255],
    [0, 140, 48],
    [38, 191, 25],
    [128, 217, 0],
    [166, 243, 0],
    [204, 255, 51],
    [166, 166, 0],
    [204, 204, 0],
    [235, 235, 0],
    [255, 255, 0],
    [255, 255, 153],
    [217, 115, 0],
    [255, 128, 0],
    [255, 158, 0],
    [255, 189, 0],
    [255, 217, 0],
    [153, 0, 0],
    [204, 0, 0],
    [255, 0, 0],
    [255, 102, 102],
    [255, 153, 153],
    [255, 191, 191],
]
temp_colormap = colors.ListedColormap(np.array(ecmwf_temp_rgb) / 255.0)
temp_norm = colors.BoundaryNorm(temp_bounds, temp_colormap.N)


# Write them in JSON files
# ------------------------


def write_in_json(jsonfile, colormap, norm):
    """Write the boundaries of the colormap into a JSON file


    Parameters
    ----------
    jsonfile: str
        Path to the JSON file to be written

    colormap: `matplotlib.colors.ListedColormap`
        The colormap to be written

    norm: `matplotlib.colors.BoundaryNorm`
        The boundaries of the color levels
    """
    with open(jsonfile, "w") as jsf:
        json.dump(
            {
                "name": os.path.basename(jsonfile)[:-4],
                "N": colormap.N,
                "bounds": norm.boundaries.tolist(),
                "colors": colormap.colors.tolist(),
            },
            jsf,
        )

    print(f"Colormap with {colormap.N} levels written in {jsonfile}")


write_in_json("temperature_colorlevels.json", temp_colormap, temp_norm)
write_in_json("radar_colorlevels.json", radar_colormap, radar_norm)
write_in_json("wind_colorlevels.json", wind_colormap, wind_norm)
