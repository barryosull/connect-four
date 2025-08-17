boot_container:
	make init
	/bin/bash

init:
	pip install -r requirements.txt
