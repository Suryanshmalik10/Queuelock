INSERT INTO jobs (type, payload, run_at)
VALUES (%(type)s, %(payload)s, COALESCE(%(run_at)s, now()));
