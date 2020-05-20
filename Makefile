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

lint_target := .

flake8:
	flake8 $(lint_target)

isortify:
	isort -rc $(lint_target)

blacken:
	black $(lint_target)

mypy:
	mypy $(lint_target)



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
