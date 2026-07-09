from pathlib import Path

from app.core.db import get_connection

SQL_DIR = Path(__file__).resolve().parents[2] / "sql"
EXPIRE_HOLD_SQL = (SQL_DIR / "expire_hold.sql").read_text()


def handle_hold_expiry(payload: dict):
    hold_id = payload["hold_id"]
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(EXPIRE_HOLD_SQL, {"hold_id": hold_id})
            rows_affected = cur.rowcount
        conn.commit()

    if rows_affected == 1:
        print(f"    -> hold {hold_id} expired")
    else:
        print(f"    -> hold {hold_id} skipped (already confirmed/expired or not yet due)")
