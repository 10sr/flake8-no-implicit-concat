check: test lint 

test:

lint: mypy flake8

flake8:
	flake8 .

isortify:
	isort -rc .

blacken:
	black .


mypy:
	mypy .

