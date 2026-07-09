UPDATE jobs SET status = 'processing', updated_at = now() WHERE id = %(job_id)s;
