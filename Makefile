install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	echo "Not implemented yet"
	#python -m pytest -vv test_*.py

build:
	#build container
	docker build -t deploy-fastapi .

run:
	#run docker
	docker run -p 127.0.0.1:8080:8080 11a4cf733e93

format:	
	black *.py src/*.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py

refactor: format lint

all: install lint deploy