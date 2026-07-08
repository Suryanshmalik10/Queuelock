"""initial schema: users, seats, holds, payments, bookings, jobs, job_locks

Revision ID: 0001
Revises:
Create Date: 2026-07-09

This migration does NOT use autogenerate. It executes the hand-written
raw SQL in Database/schema.sql, which is the real source of truth for
the schema.
"""
from pathlib import Path

from alembic import op

revision = "0001"
down_revision = None
branch_labels = None
depends_on = None

SCHEMA_SQL_PATH = Path(__file__).resolve().parents[2] / "Database" / "schema.sql"


def upgrade() -> None:
    op.execute(SCHEMA_SQL_PATH.read_text())


def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS job_locks CASCADE;")
    op.execute("DROP TABLE IF EXISTS jobs CASCADE;")
    op.execute("DROP TABLE IF EXISTS bookings CASCADE;")
    op.execute("DROP TABLE IF EXISTS payments CASCADE;")
    op.execute("DROP TABLE IF EXISTS holds CASCADE;")
    op.execute("DROP TABLE IF EXISTS seats CASCADE;")
    op.execute("DROP TABLE IF EXISTS users CASCADE;")
