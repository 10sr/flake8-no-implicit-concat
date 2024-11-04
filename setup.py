#!/usr/bin/env python

"""Setup script."""

from setuptools import setup

setup(
    # Python3.6 requires scm configs to be here
    use_scm_version={
        "write_to": "flake8_no_implicit_concat/_version.py",
        "local_scheme": "no-local-version",
    }
)
