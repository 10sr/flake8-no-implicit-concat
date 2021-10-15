[![PyPI version](https://badge.fury.io/py/flake8-no-implicit-concat.svg)](https://badge.fury.io/py/flake8-no-implicit-concat)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flake8-no-implicit-concat)
[![Downloads](https://pepy.tech/badge/flake8-no-implicit-concat/month)](https://pepy.tech/project/flake8-no-implicit-concat)
[![Github Actions](https://github.com/10sr/flake8-no-implicit-concat/workflows/build/badge.svg?event=push)](https://github.com/10sr/flake8-no-implicit-concat/actions)
[![Codecov](https://codecov.io/gh/10sr/flake8-no-implicit-concat/branch/master/graph/badge.svg)](https://codecov.io/gh/10sr/flake8-no-implicit-concat)



flake8-no-implicit-concat
=========================

[Flake8][] plugin that forbids implicit str/bytes literal concatenations.

    # NG
    a = 'abc' 'def'
    b = ["aaa",
         "bbb"
         "ccc"]
    c = b'hoge' b'fuga'

    # OK
    a = 'abcdef'
    b = ["aaa",
         "bbb" +
         "ccc"]
    c = b'hogefuga'


Installation
------------

Install via pip:

    pip install flake8-no-implicit-concat


Violation Codes
---------------

The plugin uses the prefix `NIC`, short for No Implicit Concatenation.

| Code   | Description                                                |
| ------ | ---------------------------------------------------------- |
| NIC001 | Implicitly concatenated str literals on one line           |
| NIC002 | Implicitly concatenated str literals over multiple lines   |
| NIC101 | Implicitly concatenated bytes literals on one line         |
| NIC102 | Implicitly concatenated bytes literals over multiple lines |


Other Plugins & Linters
-----------------------

- [**flake8-implicit-str-concat**][flake8-implicit-str-concat]
  Flake8 plugin to encourage correct string literal concatenation.
  This plugin is different from `flake8-no-implicit-concat`
  because this plugin prefers implicit concatenations over explicit `+`
  operators when concatenating literals over multiple lines.
- [**wemake-python-styleguide**][wemake-python-styleguide]
  Set of strict flake8 rules with several plugins as dependencies.
  It implements `WPS326 Found implicit string concatenation`, which also
  checks implicit string concatenations, as one of the many rules it defines.
- [**pylint**][pylint] 
  This linter has `implicit-str-concat` rule.
  By default it only looks for occurrences of implicit concatenations on the
  same line, but it has `--check-str-concat-over-line-jumps=y` option
  to enable checking of concatenations over multiple lines.


Development
-----------

Use tools like Pipenv:

    pipenv run python -m pip install -e .[dev]
    pipenv run make check


License
-------

This software is licensed under MIT license. See `LICENSE` for details.

The code was derived from [flake8-implicit-str-concat][], which is developed by
Dylan Turner and also licensed under MIT license.



[Flake8]: https://flake8.pycqa.org/en/latest/
[flake8-implicit-str-concat]: https://github.com/keisheiled/flake8-implicit-str-concat
[wemake-python-styleguide]: https://github.com/wemake-services/wemake-python-styleguide
[pylint]: https://github.com/PyCQA/pylint
