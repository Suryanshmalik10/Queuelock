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
