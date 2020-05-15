flake8-no-implicit-concat
=========================


Flake8 plugin to reject any implicit string concatenations.

```python
# NG
a = ["aaa",
     "bbb"
     "ccc"]
# OK
a = ["aaa",
     "bbb" +
     "ccc"]
```

Violation codes
---------------

The plugin uses the prefix `NIC`, short for Not Implicit Concatenation.

| Code   | Description                             |
| ------ | --------------------------------------- |
| NIC001 | Implicitly concatenated string literals |


Related Project
---------------

- [**flake8-implicit-str-concat**](https://github.com/keisheiled/flake8-implicit-str-concat)
  Flake8 plugin to encourage correct string literal concatenation.
  There are cases where this plugin prefers to implicit concatenation over
  explicit `+`, so these two plugins cannot be used at once.


Development
-----------

Use Pipenv to run test locally:


    pipenv install
    pipenv run check


License
=======

This software is licensed under MIT license. See `LICENSE` for details.
