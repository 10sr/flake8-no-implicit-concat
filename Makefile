check: test lint 

test:
	tests/run.sh

lint: mypy flake8

lint_target := flake8_no_implicit_concat/

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
