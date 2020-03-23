.PHONY: help test run
PYTHON_INTERPRETER ?= $(shell which python)

default: dependencies install test

help: ## This help
	@grep -E -h "^[a-zA-Z_-]+:.*?## " $(MAKEFILE_LIST) \
		| sort \
		| awk -v width=36 'BEGIN {FS = ":.*?## "} {printf "\033[36m%-*s\033[0m %s\n", width, $$1, $$2}'

dependencies:  ## Install all dependencies to build
	$(info [+] Installing dependencies...")
	pip install pipenv

install: ## installs / updates required libraries
	$(info [+] Running pipenv install, can take a while...")
	pipenv install --dev
	$(info [+] activate by running 'pipenv shell'")

test: ## runs included test suite
	$(info [+] running tests...")
	pipenv run pytest

lint: ## linting of code base for good practices
	$(info [+] linting with flake8 ...")
	# E111,E114 identention too verbose
	pipenv run flake8 app --ignore=E111,E114 