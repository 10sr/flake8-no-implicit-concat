[![Github Actions](https://github.com/10sr/flake8-no-implicit-concat/workflows/Build/badge.svg?event=push)](https://github.com/10sr/flake8-no-implicit-concat/actions)
[![codecov](https://codecov.io/gh/10sr/flake8-no-implicit-concat/branch/master/graph/badge.svg)](https://codecov.io/gh/10sr/flake8-no-implicit-concat)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flake8-no-implicit-concat)
[![PyPI version](https://badge.fury.io/py/flake8-no-implicit-concat.svg)](https://badge.fury.io/py/flake8-no-implicit-concat)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)



flake8-no-implicit-concat
=========================

Flake8 plugin that forbids any implicit string concatenations.

    # NG
    a = ["aaa",
         "bbb"
         "ccc"]
    # OK
    a = ["aaa",
         "bbb" +
         "ccc"]


Installation
------------

Install via pip:

    pip install flake8-no-implicit-concat


Violation code
--------------

The plugin uses the prefix `NIC`, short for No Implicit Concatenation.

| Code   | Description                             |
| ------ | --------------------------------------- |
| NIC001 | Implicitly concatenated string literals |


Related Projects
----------------

- [**flake8-implicit-str-concat**][flake8-implicit-str-concat]
  Flake8 plugin to encourage correct string literal concatenation.
  There are cases where this plugin prefers to implicit concatenation over
  explicit `+`, so these two plugins cannot be used at once.
- [**wemake-python-styleguide**][wemake-python-styleguide]
  Set of strict flake8 rules with some other plugins as dependencies.
  It implements `WPS326 Found implicit string concatenation`, which also 
  checks implicit string concatenations, as one of the many rules it has.


Development
-----------

Use Pipenv to run test locally:

    pipenv install
    pipenv run check


License
-------

This software is licensed under MIT license. See `LICENSE` for details.

The code was derived from [flake8-implicit-str-concat][], which is developed by
Dylan Turner and also licensed under MIT license.



[flake8-implicit-str-concat]: https://github.com/keisheiled/flake8-implicit-str-concat
[wemake-python-styleguide]: https://github.com/wemake-services/wemake-python-styleguide
