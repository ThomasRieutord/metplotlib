#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Metplotlib

https://github.com/ThomasRieutord/metplotlib
"""
import os

package_rootdir = os.path.dirname(os.path.realpath(__path__[0]))

with open(os.path.join(package_rootdir, "setup.py"), "r") as f:
    for l in f.readlines():
        if "version=" in l:
            __version__ = l.split('"')[1]
            break

del f, l, os
