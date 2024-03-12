#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Metplotlib

Main module


Notes
-----
For more info on figure/data CRS, see [here](https://scitools.org.uk/cartopy/docs/latest/tutorials/understanding_transform.html)
"""
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colormaps as mplcm

from metplotlib import colormaps as metcm

default_figsize = (12, 12)
str4x4 = np.array([["", ""], ["", ""]])


def _replace_default_figax(fig, ax, figcrs=None):
    """Replace None by default values for Figure and Axes"""
    if fig is None:
        fig = plt.figure(figsize=default_figsize)

    if ax is None:
        ax = plt.subplot(projection=figcrs)

    return fig, ax


def _replace_default_latlon(lons, lats, data):
    """Replace None by default values for longitudes and latitudes"""
    if lons is None:
        lons = np.arange(data.shape[1])
    if lats is None:
        lats = np.arange(data.shape[0])

    assert (
        lons.ndim == lats.ndim
    ), "Longitudes and latitudes do not have the same number of dimensions"
    if lons.ndim == 1:
        lons, lats = np.meshgrid(lons, lats)

    return lons, lats


# Single plots
# ------------


def isolines(
    data,
    lons=None,
    lats=None,
    fig=None,
    ax=None,
    figcrs=ccrs.PlateCarree(),
    datcrs=ccrs.PlateCarree(),
):
    """Isoline plot (e.g. for mean sea level pressure)


    Parameters
    ----------
    data: ndarray of shape (n_lons, n_lats)
        The values of the variable to plot

    lons: ndarray of shape (n_lons,) or (n_lons, n_lats)
        Longitudes values for the data points expressed in the data CRS (see `figcrs` and `datcrs`)

    lats: ndarray of shape (n_lons,) or (n_lons, n_lats)
        Latitudes values for the data points expressed in the data CRS (see `figcrs` and `datcrs`)

    fig: `matplotlib.pyplot.Figure`
        The figure object in which the plot is made. If None, a new one is created

    ax: `matplotlib.pyplot.Axes`
        The axes object in which the plot is made

    figcrs:
        Figure coordinate system. Set what the figure will look like

    datcrs:
        Data coordinate system. Describes how the data is stored


    Returns
    -------
    fig: `matplotlib.pyplot.Figure`
        The figure object in which the plot is made. If None, a new one is created

    ax: `matplotlib.pyplot.Axes`
        The axes object in which the plot is made


    Examples
    --------
    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> import cartopy.crs as ccrs
    >>> from metplotlib import plots
    >>> lon, lat = np.meshgrid(np.linspace(-20, 50, 25), np.linspace(30, 70, 25))
    >>> data = 1011 + 5*(np.cos(np.deg2rad(lat) * 4) + np.sin(np.deg2rad(lon) * 4))
    >>> fig = plt.figure()
    >>> ax = plt.axes(projection=ccrs.PlateCarree())
    >>> ax.coastlines()
    >>> fig, ax = plots.isolines(data, lon, lat, fig=fig, ax=ax)
    >>> fig.show()
    """
    fig, ax = _replace_default_figax(fig, ax, figcrs)
    lons, lats = _replace_default_latlon(lons, lats, data)

    axcl = ax.contour(lons, lats, data, colors="black", transform=datcrs)
    ax.clabel(axcl, inline=True, fontsize=10, fmt="%4.f")

    return fig, ax


def colorlevels(
    data,
    lons=None,
    lats=None,
    fig=None,
    ax=None,
    varfamily="temperature",
    clabel="",
    figcrs=ccrs.PlateCarree(),
    datcrs=ccrs.PlateCarree(),
):
    """Color levels plot (e.g. for wind speed).

    The main function here is `matplotlib.pyplot.contourf`, which uses only
    a discrete set of colors. For a continuous set of colors, please use `colorshades`


    Parameters
    ----------
    All other parameters are the same as in `isolines`

    varfamily: str
        Variable family (ex: "temperature", "radar", "wind_speed")

    clabel: str
        Label for the colorbar


    Returns
    -------
    Same as in `isolines`


    Examples
    --------
    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> import cartopy.crs as ccrs
    >>> from metplotlib import plots
    >>> lon, lat = np.meshgrid(np.linspace(-20, 50, 25), np.linspace(30, 70, 25))
    >>> data = 20 + 5*(np.cos(np.deg2rad(lat) * 4) + np.sin(np.deg2rad(lon) * 4))
    >>> fig = plt.figure()
    >>> ax = plt.axes(projection=ccrs.PlateCarree())
    >>> fig, ax = plots.colorlevels(data, lon, lat, varfamily="temperature")
    >>> fig.show()
    """
    fig, ax = _replace_default_figax(fig, ax, figcrs)
    lons, lats = _replace_default_latlon(lons, lats, data)

    colormap, norm = metcm.get_colorlevels_from_varfamily(varfamily)
    values = norm.boundaries[1:-1]

    axcf = ax.contourf(
        lons,
        lats,
        data,
        values,
        cmap=colormap,
        norm=norm,
        extend="both",
        transform=datcrs,
        vmin=values[0],
        vmax=values[-1],
    )
    cbar = plt.colorbar(
        axcf,
        ticks=values,
        extend="both",
        orientation="vertical",
        shrink=0.3,
    )

    for t in cbar.ax.get_yticklabels():
        t.set_fontsize(10)

    cbar.set_label(clabel, fontsize=10)

    return fig, ax


def colorshades(
    data,
    lons=None,
    lats=None,
    fig=None,
    ax=None,
    varfamily="temperature",
    clabel="",
    figcrs=ccrs.PlateCarree(),
    datcrs=ccrs.PlateCarree(),
):
    """Color levels plot (e.g. for wind speed).

    The main function here is `matplotlib.pyplot.pcolormesh`, which uses only
    a continuous set of colors. For a discrete set of colors, please use `colorlevels`


    Parameters
    ----------
    Same as in `colorlevels`


    Returns
    -------
    Same as in `colorlevels`
    """
    fig, ax = _replace_default_figax(fig, ax, figcrs)
    lons, lats = _replace_default_latlon(lons, lats, data)

    colormap = metcm.get_colormap_from_varfamily(varfamily)

    axpc = ax.pcolormesh(
        lons,
        lats,
        data,
        cmap=colormap,
        transform=datcrs,
    )
    cbar = plt.colorbar(
        axpc,
        extend="both",
        orientation="vertical",
        shrink=0.3,
    )

    for t in cbar.ax.get_yticklabels():
        t.set_fontsize(10)

    cbar.set_label(clabel, fontsize=10)

    return fig, ax


def plumes(
    data,
    x=None,
    fig=None,
    ax=None,
    color="cornflowerblue",
    title=None,
    xlabel=None,
    ylabel=None,
):
    """Plumes showing the dispersion of an ensemble forecast


    Parameters
    ----------
    data: ndarray of shape (n_mbr, n_ldt)
        Data values with the first dimension being the ensemble

    x: ndarray of shape (n_ldt,)
        Coordinate values for the other dimension (usually the leadtime)

    fig: `matplotlib.pyplot.Figure`
        The figure object in which the plot is made. If None, a new one is created

    ax: `matplotlib.pyplot.Axes`
        The axes object in which the plot is made

    color: str or RGBA tuple
        Color of the plumes

    title: str
        Title of the plot

    xlabel: str
        Label for the x-axis

    ylabel: str
        Label for the y-axis


    Returns
    -------
    fig: `matplotlib.pyplot.Figure`
        The figure object in which the plot is made. If None, a new one is created

    ax: `matplotlib.pyplot.Axes`
        The axes object in which the plot is made
    """
    fig, ax = _replace_default_figax(fig, ax)

    n_mbr, n_ldt = data.shape

    if x is None:
        x = np.arange(n_ldt)

    for i in range(n_mbr):
        ax.plot(x, data[i, :], linestyle="--", color=color, alpha=0.2)

    ax.grid()
    if title is not None:
        ax.set_title(title)
    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)

    return fig, ax


def quantiles(
    data,
    x=None,
    quantiles=[0.1, 0.25, 0.5, 0.75, 0.9],
    fig=None,
    ax=None,
    colormap="twilight",
    title=None,
    xlabel=None,
    ylabel=None,
):
    """Plot the evolution of quantiles against another dimension (usually the lead time)


    Parameters
    ----------
    All other parameters are the same as in `plumes`

    quantiles: list of float
        List of quantiles to be plotted

    colormap: str
        The colormap to apply to the quantile values (better be a cyclic one)


    Returns
    -------
    Same as in `plumes`
    """
    fig, ax = _replace_default_figax(fig, ax)
    cmap = mplcm[colormap]

    n_mbr, n_ldt = data.shape
    if x is None:
        x = np.arange(n_ldt)

    qvalues = np.quantile(data, quantiles, axis=0)

    for i in range(len(quantiles) // 2):
        ax.plot(
            x,
            qvalues[i, :],
            color=cmap(quantiles[i]),
            linestyle="--",
            label=f"Quantile {quantiles[i]}",
        )
        ax.plot(
            x,
            qvalues[-i - 1, :],
            color=cmap(quantiles[-i - 1]),
            linestyle="--",
            label=f"Quantile {quantiles[-i-1]}",
        )
        ax.fill_between(
            x, qvalues[i, :], qvalues[-i - 1, :], color=cmap(quantiles[i]), alpha=0.2
        )

    if len(quantiles) % 2 == 1:
        i = len(quantiles) // 2
        ax.plot(
            x,
            qvalues[i, :],
            color=cmap(quantiles[i]),
            linestyle="-",
            label=f"Quantile {quantiles[i]}",
        )

    ax.grid()
    ax.legend()
    if title is not None:
        ax.set_title(title)
    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)

    return fig, ax


# Multple plots
# -------------


def twovar_plot(
    il_data,
    cl_data,
    lons=None,
    lats=None,
    cl_varfamily="temp",
    title=None,
    clabel=None,
    figcrs=ccrs.PlateCarree(),
    datcrs=ccrs.PlateCarree(),
):
    """Plot two variable on the same graph


    Parameters
    ----------
    il_data: ndarray of shape (n_lons, n_lats)
        Data to plot in isolines

    cl_data: ndarray of shape (n_lons, n_lats)
        Data to plot in color levels

    lons: ndarray of shape (n_lons,) or (n_lons, n_lats)
        Longitudes values for the data points expressed in the data CRS (see `figcrs` and `datcrs`)

    lats: ndarray of shape (n_lons,) or (n_lons, n_lats)
        Latitudes values for the data points expressed in the data CRS (see `figcrs` and `datcrs`)

    cl_varfamily: str
        Variable family for the color levels (ex: "temperature", "radar", "wind_speed")

    title: str
        Title of the graph

    clabel: str
        Colorbar label

    figcrs:
        Figure coordinate system. Set what the figure will look like

    datcrs:
        Data coordinate system. Describes how the data is stored



    Returns
    -------
    fig: `matplotlib.pyplot.Figure`
        The figure object in which the plot is made. If None, a new one is created

    ax: `matplotlib.pyplot.Axes`
        The axes object in which the plot is made


    Examples
    --------
    >>> import numpy as np
    >>> from metplotlib import plots
    >>> lon, lat = np.meshgrid(np.linspace(-20, 50, 25), np.linspace(30, 70, 25))
    >>> z500 = 1013 + 5*(np.cos(np.deg2rad(lat) * 4) + np.sin(np.deg2rad(lon) * 4))
    >>> t500 = 20.1 + 4*(np.cos(np.deg2rad(lat) * 4) + np.sin(np.deg2rad(lon) * 4))
    >>> fig, ax = plots.twovar_plot(z500, t500, lons=lon, lats=lat)
    >>> fig.show()
    """
    fig = plt.figure(figsize=default_figsize)
    ax = plt.subplot(projection=figcrs)
    ax.coastlines(resolution="50m", color="black", linewidth=0.5)

    fig, ax = isolines(il_data, lons=lons, lats=lats, fig=fig, ax=ax, datcrs=datcrs)
    fig, ax = colorlevels(
        cl_data,
        varfamily=cl_varfamily,
        lons=lons,
        lats=lats,
        clabel=clabel,
        fig=fig,
        ax=ax,
        datcrs=datcrs,
    )

    grd = ax.gridlines(draw_labels=True, linestyle="--")
    grd.top_labels = False
    grd.right_labels = False

    if title is not None:
        ax.set_title(title)

    return fig, ax


def twovar_comparison(
    il_data0,
    il_data1,
    cl_data0,
    cl_data1,
    lons=None,
    lats=None,
    cl_varfamily="temp",
    titles=str4x4,
    clabels=str4x4,
    figcrs=ccrs.PlateCarree(),
    datcrs=ccrs.PlateCarree(),
):
    """Four (2x2) subplots to compare a two-variable plot in two situations.

    It is assumed that we have two situations (0 and 1; e.g. two leadtimes or two members) and two variables (A and B).
    Upper-left shows A and B in situation 0.
    Upper-right shows A and B in situation 1.
    Lower-left shows differences (sit 0 - sit 1) in A.
    Lower-right shows differences (sit 0 - sit 1) in B.


    Parameters
    ----------
    il_data0: ndarray of shape (n_lons, n_lats)
        Data to plot in isolines valid at the situation 0

    il_data1: ndarray of shape (n_lons, n_lats)
        Data to plot in isolines valid at the situation 1

    cl_data0: ndarray of shape (n_lons, n_lats)
        Data to plot in color levels valid at the situation 0

    cl_data1: ndarray of shape (n_lons, n_lats)
        Data to plot in color levels valid at the situation 1

    lons: ndarray of shape (n_lons,) or (n_lons, n_lats)
        Longitudes values for the data points expressed in the data CRS (see `figcrs` and `datcrs`)

    lats: ndarray of shape (n_lons,) or (n_lons, n_lats)
        Latitudes values for the data points expressed in the data CRS (see `figcrs` and `datcrs`)

    cl_varfamily: str
        Variable family for the color levels (ex: "temperature", "radar", "wind_speed")

    titles: ndarray of shape (2,2)
        Titles for each subplot

    clabels: ndarray of shape (2,2)
        Colorbar label for each subplot

    figcrs:
        Figure coordinate system. Set what the figure will look like

    datcrs:
        Data coordinate system. Describes how the data is stored



    Returns
    -------
    fig: `matplotlib.pyplot.Figure`
        The figure object in which the plot is made. If None, a new one is created

    ax: `matplotlib.pyplot.Axes`
        The axes object in which the plot is made


    Examples
    --------
    >>> import numpy as np
    >>> from metplotlib import plots
    >>> lon, lat = np.meshgrid(np.linspace(-20, 50, 25), np.linspace(30, 70, 25))
    >>> cl0 = 20 + 5*(np.cos(np.deg2rad(lat) * 4) + np.sin(np.deg2rad(lon) * 4))
    >>> cl1 = 20.1 + 4*(np.cos(np.deg2rad(lat) * 4) + np.sin(np.deg2rad(lon) * 4))
    >>> iso0 = 1013 + 5*(np.cos(np.deg2rad(lat) * 4) + np.sin(np.deg2rad(lon) * 4))
    >>> iso1 = 1015 + 6*(np.cos(np.deg2rad(lat) * 4) + np.sin(np.deg2rad(lon) * 4))
    >>> fig, ax = plots.twovar_comparison(iso0, iso1, cl0, cl1, lons=lon, lats=lat)
    >>> fig.show()
    """
    fig, axs = plt.subplots(
        nrows=2, ncols=2, figsize=default_figsize, subplot_kw={"projection": figcrs}
    )
    land_50m = cfeature.NaturalEarthFeature(
        "physical", "land", "50m", edgecolor="face", facecolor=cfeature.COLORS["land"]
    )

    for ax, title in zip(axs.flatten(), titles.flatten()):
        ax.add_feature(land_50m, alpha=0.5)
        ax.coastlines(resolution="50m", color="black", linewidth=0.5)
        ax.set_title(title)
        grd = ax.gridlines(draw_labels=True, linestyle="--")
        grd.top_labels = False
        grd.right_labels = False

    ### axs[0, 0]

    fig, axs[0, 0] = isolines(
        il_data0, lons=lons, lats=lats, fig=fig, ax=axs[0, 0], datcrs=datcrs
    )
    fig, axs[0, 0] = colorlevels(
        cl_data0,
        lons=lons,
        lats=lats,
        varfamily=cl_varfamily,
        clabel=clabels[0, 0],
        fig=fig,
        ax=axs[0, 0],
        datcrs=datcrs,
    )

    ### axs[0, 1]

    fig, axs[0, 1] = isolines(
        il_data1, lons=lons, lats=lats, fig=fig, ax=axs[0, 1], datcrs=datcrs
    )
    fig, axs[0, 1] = colorlevels(
        cl_data1,
        lons=lons,
        lats=lats,
        varfamily=cl_varfamily,
        clabel=clabels[0, 1],
        fig=fig,
        ax=axs[0, 1],
        datcrs=datcrs,
    )

    ### axs[1, 0]

    fig, axs[1, 0] = colorshades(
        il_data0 - il_data1,
        lons=lons,
        lats=lats,
        varfamily="diff",
        clabel=clabels[1, 0],
        fig=fig,
        ax=axs[1, 0],
        datcrs=datcrs,
    )

    ### axs[1, 1]

    fig, axs[1, 1] = colorshades(
        cl_data0 - cl_data1,
        lons=lons,
        lats=lats,
        varfamily="diff",
        clabel=clabels[1, 1],
        fig=fig,
        ax=axs[1, 1],
        datcrs=datcrs,
    )

    fig.tight_layout()

    return fig, axs


# EOF
