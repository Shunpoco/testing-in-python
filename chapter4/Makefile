install:
	pip install --upgrade pip && \
	pip intall -r requirements.txt

test:
	python -m pytest -vv test_hello.py

lint:
	pylint --disable=R,C hello.py

all: install lint test
