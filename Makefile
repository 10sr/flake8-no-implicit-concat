check: test lint

test:

lint:
	flake8 .

isortify:
	isort -rc .

blacken:
	black .
