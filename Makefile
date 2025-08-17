boot_container:
	make init
	/bin/bash

init:
	pip install -r requirements.txt

run:
	python src/main.py

test:
	pytest tests
