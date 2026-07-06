## Understanding `.env`, `config.py`, and `db.py`

These three files work together to let the application connect to PostgreSQL in a clean and secure way.

### `.env`
- Stores configuration values such as the database URL, API keys, timeouts, and other settings.
- Keeps sensitive information out of the source code.
- Different environments (development, testing, production) can use different `.env` files without changing the application code.

### `config.py`
- Reads the `.env` file **once** when the application starts.
- Makes all configuration values available to the rest of the application through a single `settings` object.
- Prevents every file from reading `.env` separately.

### `db.py`
- Uses the values from `config.py` to establish a connection with PostgreSQL.
- Creates a database session whenever FastAPI needs to interact with the database.
- Automatically closes the session after the request finishes, preventing connection leaks.

---

### Responsibilities (Quick Revision)

- **`.env`** → Stores configuration values (database URL, timeouts, secrets, etc.).
- **`config.py`** → Reads `.env` once and makes those values available to the entire application.
- **`db.py`** → Uses those values to connect to PostgreSQL and provides a database session whenever FastAPI needs one.