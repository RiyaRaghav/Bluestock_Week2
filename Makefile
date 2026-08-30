install:
	pip install -r requirements.txt

test:
	python -m pytest

load:
	python src/etl/loader.py

all: install load test