# PostgreSQL Setup (Ubuntu VM)

## Install PostgreSQL

```bash
sudo apt update
sudo apt install -y postgresql postgresql-contrib

Create User
sudo -u postgres psql -c "CREATE USER queuelock WITH PASSWORD 'queuelock';"

Creates a PostgreSQL role for the application.

Create Database
sudo -u postgres psql -c "CREATE DATABASE queuelock OWNER queuelock;"

Creates the application database owned by the created user.
