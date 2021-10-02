check: test lint 

test: test-runflake8 test-pytest


test-runflake8:
	tests/run_flake8/Run.sh

test-pytest:
	coverage erase
	coverage run -m unittest discover -v  # tests/test_*.py
	coverage xml --fail-under 90

codecov:
	codecov


lint: mypy flake8

flake8:
	flake8 --version
	flake8 .

isortify:
	isort -rc .

blacken:
	black .

mypy:
	# Temporarily check only package directory
	mypy --strict flake8_no_implicit_concat/



sdist:
	python setup.py sdist

wheel:
	python setup.py bdist_wheel

publish_repository ?= testpypi
publish: sdist wheel
	twine upload --repository $(publish_repository) dist/*

# Do not add to devdependencies because different platforms install
# different packages
publish-installdeps:
	pip install twine wheel
