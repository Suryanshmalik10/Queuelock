SELECT id, type, payload, attempts
FROM jobs
WHERE status = 'pending' AND run_at <= now()
ORDER BY run_at
LIMIT 1
FOR UPDATE SKIP LOCKED;
