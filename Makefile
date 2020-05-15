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

