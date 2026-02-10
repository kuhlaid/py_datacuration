# This file simplifies the commands needed to manage this package and requirements.

# Variables
PYTHON = python3
VENV_DIR = .venv

# since we are running the venv from the Makefile, the venv is not activating and thus `VIRTUAL_ENV` is not automatically exported as an environment variable
# here we set the absolute path to the virtual environment
export VIRTUAL_ENV = $(VENV_DIR)

# creates a virtual environment for the package 
# `make venvCreate`
venvCreate:
	( \
		rm -rf $(VENV_DIR); \
		$(PYTHON) -m venv $(VENV_DIR); \
		. $(VENV_DIR)/bin/activate; \
		pip install --upgrade pip; \
	)

# here is where we add requirements/packages to our virtual environment if they are missing after running the `testVenv` command
# `make installRequirements`
installRequirements:
	( \
		. $(VENV_DIR)/bin/activate; \
		pip install humanize ipynbname nbconvert pandas pydantic pydantic_core pymysql sqlalchemy; \
	)

# test the virtual environment to ensure requirements are met for each of our scripts
# `make testVenv`
testVenv:
	( \
		. $(VENV_DIR)/bin/activate; \
		$(VENV_DIR)/bin/python tester.py; \
	)

# create a requirements file from the current venv
# `make pipFreeze`
pipFreeze:
	( \
       . $(VENV_DIR)/bin/activate; \
       pip freeze > requirements.txt; \
    )

# run the local server instance `make updateRequirements`
updateRequirements:
	( \
		. $(VENV_DIR)/bin/activate; \
		$(VENV_DIR)/bin/pip install -r requirements.txt; \
	)

# makes the Python wheel for the app using 
# `make createWheel`
createWheel:
	( \
       . $(VENV_DIR)/bin/activate; \
       $(VENV_DIR)/bin/pip install build; \
	   $(VENV_DIR)/bin/python -m build --wheel; \
    )

