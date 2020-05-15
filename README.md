flake8-no-implicit-concat
=========================


Flake8 plugin to reject any implicit string concatenations.

```python
# NG
a = ("String with "
     "implicit concatenation")
# OK
b = ("Explicitly concatenated " +
     "string")
```

Development
-----------

Use Pipenv to run test locally:


    pipenv install
    pipenv run check
