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
	python -m pytest src/{{ cookiecutter.package_name }}/tests

coverage: ## check code coverage quickly with the default Python
	coverage run --source src/{{ cookiecutter.package_name }} -m pytest
	coverage report -m
	coverage html

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	pip install --extra-index-url https://$(ARTIFACTORY_USER):$(ARTIFACTORY_PASSWORD)@fundingcircle.jfrog.io/fundingcircle/api/pypi/pypi/simple .

install-dev: clean ## install the package to the active Python's site-packages
	pip install --extra-index-url https://$(ARTIFACTORY_USER):$(ARTIFACTORY_PASSWORD)@fundingcircle.jfrog.io/fundingcircle/api/pypi/pypi/simple .[dev]

release: dist
	twine upload --repository-url https://fundingcircle.jfrog.io/fundingcircle/api/pypi/pypi-local -u $(ARTIFACTORY_USER) -p $(ARTIFACTORY_PASSWORD) dist/*

snapshot-release:
	twine upload --repository-url https://fundingcircle.jfrog.io/fundingcircle/api/pypi/pypi-snapshots-local -u $(ARTIFACTORY_USER) -p $(ARTIFACTORY_PASSWORD) dist/*

