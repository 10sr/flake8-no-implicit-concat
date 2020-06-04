#!/usr/bin/env python

"""Setup script."""

from setuptools import setup


def _get_version() -> str:
    with open("flake8_no_implicit_concat/_version.py") as f:
        for line in f:
            if line.startswith("__version__"):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


setup(
    version=_get_version(),
    entry_points={"flake8.extension": ["NIC = flake8_no_implicit_concat:Checker"]},
)
