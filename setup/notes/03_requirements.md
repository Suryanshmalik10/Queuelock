# Project Dependencies (requirements.txt)

The `requirements.txt` file contains all the Python packages required to run this project. It ensures every developer installs the same package versions, making the project consistent across different systems.

---

## Install Dependencies

```bash
pip install -r setup/requirements.txt
```

Installs all the required packages listed in `requirements.txt`.

---

## FastAPI

```txt
fastapi==0.115.0
```

FastAPI is the backend web framework used to build high-performance REST APIs with automatic request validation and interactive API documentation.

---

## Uvicorn

```txt
uvicorn[standard]==0.30.6
```

Uvicorn is the ASGI server that runs the FastAPI application during development and deployment.

---

## SQLAlchemy

```txt
sqlalchemy==2.0.35
```

SQLAlchemy is the ORM (Object Relational Mapper) used to communicate with the PostgreSQL database using Python objects.

---

## psycopg2-binary

```txt
psycopg2-binary==2.9.9
```

A PostgreSQL database driver that allows Python applications and SQLAlchemy to connect to PostgreSQL.

---

## Alembic

```txt
alembic==1.13.2
```

Alembic is used for database schema migrations, allowing database changes to be version controlled.

---

## Pydantic

```txt
pydantic==2.9.2
```

Pydantic validates request and response data, ensuring only correctly formatted data enters the application.

---

## Pydantic Settings

```txt
pydantic-settings==2.5.2
```

Provides an easy way to manage application configuration using environment variables and `.env` files.

---

## Python Dotenv

```txt
python-dotenv==1.0.1
```

Loads environment variables from a `.env` file, keeping sensitive information such as database credentials outside the source code.
