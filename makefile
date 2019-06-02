make:
	vim makefile

venv:
	virtualenv -p python3 venv

deps:
	./venv/bin/pip3 install -r requirements.txt

test:
	./venv/bin/python -m unittest discover -p *_test.py

runescape_login:
	./venv/bin/python runescape_login.py

runescape_fire:
	./venv/bin/python runescape_fire.py

shell:
	./venv/bin/ipython
