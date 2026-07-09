
from alembic import op

revision = "0002"
down_revision = "0001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("ALTER TABLE jobs DROP CONSTRAINT jobs_type_check;")
    op.execute("""
        ALTER TABLE jobs
        ADD CONSTRAINT jobs_type_check
        CHECK (type IN ('hold_expiry', 'payment_confirm', 'test_echo'));
    """)


def downgrade() -> None:
    op.execute("ALTER TABLE jobs DROP CONSTRAINT jobs_type_check;")
    op.execute("""
        ALTER TABLE jobs
        ADD CONSTRAINT jobs_type_check
        CHECK (type IN ('hold_expiry', 'payment_confirm'));
    """)
