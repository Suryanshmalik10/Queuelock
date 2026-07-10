SELECT b.id, b.user_id, b.seat_id, b.payment_id, b.status, b.booked_at,s.seat_number,
u.name AS user_name
FROM bookings b
JOIN seats s ON s.id = b.seat_id
JOIN users u ON u.id = b.user_id
ORDER BY b.booked_at DESC;