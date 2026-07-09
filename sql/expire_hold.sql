UPDATE holds
SET status = 'expired'
WHERE id = %(hold_id)s
  AND status = 'active'
  AND expires_at <= now();
