.PHONY: build venv deps clean init kernel

build: venv deps init

venv:
	virtualenv -p python3 .env

deps:
	.env/bin/pip install -r requirements.txt

clean:
	find -name '*.pyc' -delete
	find -name '*.swp' -delete
	find -name '__pycache__' -delete

kernel:
	. .env/bin/activate && \
		ipython kernel install --user --name=mlzoomcamp-venv

init:
	if [ ! -e var/run ]; then mkdir -p var/run; fi
	if [ ! -e var/log ]; then mkdir -p var/log; fi
