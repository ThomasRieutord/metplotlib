#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Metplotlib

Testing of ensemble plots on fake data.
"""

import numpy as np

from metplotlib import plots

n_mbr = 51
n_ldt = 72

leadtimes = np.arange(n_ldt)
temp = np.ones((n_mbr, n_ldt))
for i in range(n_mbr):
    temp[i, :] = (
        15
        * np.sin(
            np.pi * leadtimes / (24 + 1.5 * np.random.random())
            + 0.8 * np.random.random()
        )
        + 5 * np.random.random()
    )


def test_plumes():
    fig, ax = plots.plumes(temp, x=leadtimes)
    fig.show()
    assert fig and ax


def test_quantiles():
    fig, ax = plots.quantiles(temp, x=leadtimes)
    fig.show()
    assert fig and ax


if __name__ == "__main__":
    test_plumes()
    test_quantiles()
