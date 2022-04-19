# poetry activate environment

poetry shell


# By default, poetry creates a virtual environment in {cache-dir}/virtualenvs

poetry env list

poetry env remove poet-L6vOte6N-py3.8

poetry config --list

# Setting env path
poetry config virtualenvs.in-project true 
OR 
poetry.toml (Create file)

[virtualenvs]
create = true
in-project = true

Link: https://github.com/python-poetry/poetry/issues/108


# Format code tools
black --check --diff --color .

black {source_file_or_directory}


# Unitest

coverage run -m unittest discover --pattern "test_*.py"

coverage report -m

# Channel Connector App
Generic / normalized marketplace connector

## Built With
* [FastAPI](https://fastapi.tiangolo.com/)
* [Python](https://www.python.org/downloads/)

## Quick Start (Local)
1. Install Python & Poetry.
2. Use command `pip install poetry`
3. Use command `cp .env.example .env`
4. Replace the BEARER_TOKEN environment variable in the .env file.
5. Use command `poetry install`
6. Use command `. .venv/bin/activate`
7. Use command `uvicorn main:app` or `python main.py` to run the application.


## Commands

### Black - Code Format
Applies formatting to all source code files.
Use command: `black .`

### Flake8 - Enforces defined style on the source code files.
Checks the source code files for conformity.
Use command: `flake8 .`

### Isort - Sort Imports
Applies sorting to imports in source code files.
Use command: `isort .`

### Safety - Checks dependencies for vulnerabilities
Outputs a report of which dependencies to upgrade.
Use command: `safety check --full-report`

### Run All Unit Tests and Coverage Report
1. Rules:
   * The `tests` folders should remain inside the component folder which they relate
   * Add the `__init__.py` file in each folder and `tests` folder
   * Tests file use pattern as `test_*.py`
   

2. Commands:

   2.1. Run All Unit Tests:`python -m unittest discover --pattern "test_*.py"`

   2.2. Coverage Report:

   `coverage run -m unittest discover --pattern "test_*.py"`

   `coverage report -m`
