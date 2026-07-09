import json
from pathlib import Path

from app.core.db import get_connection

SQL_DIR = Path(__file__).resolve().parents[2] / "sql"


def _load_sql(filename: str) -> str:
    return (SQL_DIR / filename).read_text()


ENQUEUE_SQL = _load_sql("enqueue_job.sql")
DEQUEUE_SQL = _load_sql("dequeue_job.sql")
MARK_PROCESSING_SQL = _load_sql("mark_job_processing.sql")
MARK_DONE_SQL = _load_sql("mark_job_done.sql")
MARK_FAILED_SQL = _load_sql("mark_job_failed.sql")


def enqueue(job_type: str, payload: dict, run_at=None):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(ENQUEUE_SQL, {
                "type": job_type,
                "payload": json.dumps(payload),
                "run_at": run_at,
            })
        conn.commit()


def dequeue_and_process(handler_map: dict, worker_name: str = "worker"):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(DEQUEUE_SQL)
            job = cur.fetchone()

            if job is None:
                conn.commit()
                return None

            cur.execute(MARK_PROCESSING_SQL, {"job_id": job["id"]})

            try:
                handler = handler_map.get(job["type"])
                if handler is None:
                    raise ValueError(f"No handler registered for job type: {job['type']}")

                handler(job["payload"])

                cur.execute(MARK_DONE_SQL, {"job_id": job["id"]})
                conn.commit()
                print(f"[{worker_name}] done   job id={job['id']} type={job['type']}")

            except Exception as e:
                conn.rollback()
                with conn.cursor() as fail_cur:
                    fail_cur.execute(MARK_FAILED_SQL, {"job_id": job["id"]})
                conn.commit()
                print(f"[{worker_name}] FAILED job id={job['id']} type={job['type']} error={e}")

            return job
