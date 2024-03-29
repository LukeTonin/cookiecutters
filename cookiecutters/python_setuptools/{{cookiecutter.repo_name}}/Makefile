.PHONY: help clean clean-build clean-pyc clean-test check-format test coverage dist install 
.DEFAULT_GOAL := help

help: ## display this help screen
	@grep -E '^[a-z.A-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

check-format: ## check style with black
	black --check src

format: ## check style with black
	black src

test: ## run tests quickly with the default Python
	python -m pytest src/{{ cookiecutter.project_slug }}/tests

coverage: ## check code coverage quickly with the default Python
	coverage run --source {{ cookiecutter.project_slug }} -m pytest
	coverage report -m
	coverage html

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	pip install .

install-dev: clean ## install the package to the active Python's site-packages
	pip install .[dev]