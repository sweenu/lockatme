init:
	pip install pipenv
	pipenv install --dev

test:
	pipenv run pytest tests

flake8:
	pipenv run flake8
