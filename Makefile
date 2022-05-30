.PHONY: all help install test format lint

help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo "  install     to install the necessary dependencies for jupyter-book to build"
	@echo "  test        to test"
	@echo "  debug       to invoke a debugger"
	@echo "  format      to format scripts"
	@echo "  lint        to lint scripts"
	
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vvv --cov=hello --cov=greeting --cov=smath --cov=web tests 
	python -m pytest -vv --pdb 
	python -m pytest -nbval *.ipynb

debug:
	python -m pytest -vv --pdb 

format:
	black *.py
	isort *.py

lint:
	pylint --disable=R,C hello.py

all: install format lint test