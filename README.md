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

Link: https://github.com/psf/black

# Unitest

coverage run -m unittest discover --pattern "test_*.py"

coverage report -m