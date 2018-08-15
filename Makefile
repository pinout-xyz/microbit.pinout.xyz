.PHONY: check-venv check-not-venv usage resources

usage:
	@echo "usage:  make <target>"
	@echo "venv:   Create a Python virtual environment and install requirements"
	@echo "html:   Build the website HTML" 

html: build check-venv
	python build.py

resources: build
	cp -r resources/* build/resources/

build:
	mkdir build
	mkdir build/resources

venv: check-not-venv requirements.txt
	python -m virtualenv venv
	. venv/bin/activate; printf "Entering Virtual Environment: $$VIRTUAL_ENV\n"; pip install -r requirements.txt
	@echo "Virtual Environment prepared, use \"source venv/bin/activate\" to activate."

check-venv:
ifndef VIRTUAL_ENV
	$(error Not currently running in a Python Virtual Environment, run "source ./venv/bin/activate" first)
endif

check-not-venv:
ifdef VIRTUAL_ENV
	$(error Currently running a Python Virtual Environment, run "deactivate" first)
endif


