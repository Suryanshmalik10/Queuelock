# Python Virsion issue

Issue: Ubuntu 26.04 ships with Python 3.14, which was incompatible with pydantic-core used by the project.

Solution:

Installed Python 3.13.13 using pyenv.
Created the virtual environment using Python 3.13.
Updated psycopg2-binary from 2.9.9 to 2.9.11 in setup/requirements.txt.
Reinstalled dependencies successfully.

## What is `__init__.py`?

`__init__.py` tells Python that a directory should be treated as a package. It allows files inside that directory to be imported using package syntax. It can also execute initialization code and expose commonly used classes or functions when the package is imported. In this project, `app/models/__init__.py` imports all SQLAlchemy models so they are registered automatically.