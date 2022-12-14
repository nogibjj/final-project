install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

run:
	python3 main.py

format:	
	black *.py mylib/*.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py

refactor: format lint

all: install format lint run