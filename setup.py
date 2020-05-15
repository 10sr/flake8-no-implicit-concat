#!/usr/bin/env python

"""Setup script."""

from setuptools import setup

setup(
    entry_points={
        "flake8.extension": ["NIC = flake8_no_implicit_concat.checker:Checker"]
    }
)
