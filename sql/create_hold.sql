INSERT INTO holds (user_id, seat_id, expires_at)
VALUES (%(user_id)s, %(seat_id)s, now() + (%(ttl_seconds)s || ' seconds')::interval)
RETURNING id, user_id, seat_id, status, expires_at;