SELECT id, seat_id, user_id, status, expires_at
FROM holds
WHERE id = %(hold_id)s
FOR UPDATE;

SELECT id, status
FROM seats
WHERE id = %(seat_id)s
FOR UPDATE;

INSERT INTO bookings (user_id, seat_id, payment_id, status)
VALUES (%(user_id)s, %(seat_id)s, %(payment_id)s, 'confirmed')
RETURNING id;

UPDATE holds SET status = 'confirmed' WHERE id = %(hold_id)s;

UPDATE seats SET status = 'booked' WHERE id = %(seat_id)s;