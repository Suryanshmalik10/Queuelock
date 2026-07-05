# Python Virtual Environment

## Activate Environment

```bash
source venv/bin/activate
```

Activates the Python virtual environment so all installed packages remain isolated from the system Python.

---

## Install Dependencies

```bash
pip install -r setup/requirements.txt
```

Installs all the required Python packages listed in the `requirements.txt` file.

---

## View Installed Packages

```bash
pip list
```

Displays all Python packages currently installed in the active virtual environment.

---

## Freeze Installed Packages

```bash
pip freeze > setup/requirements.txt
```

Updates the `requirements.txt` file with the exact versions of all installed packages.

---

## Deactivate Environment

```bash
deactivate
```

Exits the virtual environment and returns to the system's default Python environment.
