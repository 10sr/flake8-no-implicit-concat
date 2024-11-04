check: test lint

test: test-runflake8 test-pytest


test-runflake8:
	tests/run_flake8/Run.sh

test-pytest:
	coverage erase
	coverage run -m unittest discover -v  # tests/test_*.py
	coverage xml

codecov:
	codecov


lint: mypy flake8

flake8:
	flake8 --version
	flake8 .

isortify:
	isort .

blacken:
	black .

mypy:
	# Temporarily check only package directory
	mypy --strict flake8_no_implicit_concat/



sdist:
	python setup.py sdist

wheel:
	python setup.py bdist_wheel

publish_repository ?= testpypi  # Set to pypi to publish as production
publish: sdist wheel
	twine upload --skip-existing --verbose --repository $(publish_repository) dist/*

# Do not add to devdependencies because different platforms install
# different packages
publish-installdeps:
	pip install twine wheel setuptools
