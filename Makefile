install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest --nbval src/*.ipynb
	python -m pytest -vv --cov=main tests/test_*.py

format:	
	black *.py 

lint:
	nbqa ruff src/*.ipynb
	ruff check src/*.py
		
all: install lint test format
