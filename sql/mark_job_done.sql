UPDATE jobs SET status = 'done', updated_at = now() WHERE id = %(job_id)s;
