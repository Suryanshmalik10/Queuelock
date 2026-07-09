UPDATE jobs
SET status = 'failed', attempts = attempts + 1, updated_at = now()
WHERE id = %(job_id)s;
