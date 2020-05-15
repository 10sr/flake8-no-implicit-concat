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

Development
-----------

Use Pipenv to run test locally:


    pipenv install
    pipenv run check
