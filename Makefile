VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

install:
	@test -d $(VENV) || python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

fetch:
	$(PYTHON) scripts/fetch_filtered_metadata.py --filter year --min_year 2020 --limit 100

fetch-insecure:
	$(PYTHON) scripts/fetch_filtered_metadata.py --filter year --min_year 2010 --limit 100 --insecure

prepare-mit-demo:
	$(PYTHON) scripts/download_mit_demo.py

test:
	$(PYTHON) -m pytest -vv tests/

format:
	$(VENV)/bin/black src/ tests/ scripts/

lint:
	$(VENV)/bin/pylint --disable=R,C src/ tests/ scripts/

all: install lint test

sql-db:
	$(PYTHON) scripts/sql_db.py

eda:
	PYTHONPATH=. $(PYTHON) scripts/eda.py