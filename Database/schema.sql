CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);


CREATE TABLE seats(
    id SERIAL PRIMARY KEY,
    seat_number TEXT NOT NULL UNIQUE,
    status TEXT NOT NULL DEFAULT 'available'
           CHECK (status IN('available','held','booked')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- A hold is a temporary claim on a seat while a user pays.
CREATE TABLE holds(
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    seat_id INT NOT NULL REFERENCES seats(id) ON DELETE CASCADE,
    status TEXT NOT NULL DEFAULT 'active'
           CHECK (status IN ('active', 'expired', 'confirmed')),
    expires_at TIMESTAMPTZ NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Only one *active* hold should exist per seat at a time.
CREATE UNIQUE INDEX uq_holds_active_seat
    ON holds (seat_id)
    WHERE status = 'active';


CREATE TABLE payments(
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    hold_id INT NOT NULL REFERENCES holds(id) ON DELETE CASCADE,
    amount NUMERIC(10, 2) NOT NULL CHECK (amount > 0),
    status TEXT NOT NULL DEFAULT 'pending'
           CHECK (status IN ('pending', 'confirmed', 'failed')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);


CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    seat_id INT NOT NULL REFERENCES seats(id) ON DELETE CASCADE,
    payment_id INT NOT NULL REFERENCES payments(id) ON DELETE CASCADE,
    status TEXT NOT NULL DEFAULT 'confirmed'
           CHECK (status IN ('confirmed', 'cancelled')),
    booked_at TIMESTAMPTZ NOT NULL DEFAULT now()
);


-- a seat can only have ONE confirmed booking, ever.
CREATE UNIQUE INDEX uq_bookings_confirmed_seat
    ON bookings (seat_id)
    WHERE status = 'confirmed';


CREATE TABLE jobs(
    id SERIAL PRIMARY KEY,
    type TEXT NOT NULL CHECK (type IN ('hold_expiry', 'payment_confirm', 'test_echo')),
    payload JSONB NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending'
           CHECK (status IN ('pending', 'processing', 'done', 'failed')),
    run_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    attempts INT NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);


CREATE INDEX idx_jobs_dequeue ON jobs (status, run_at);


CREATE TABLE job_locks (
    id SERIAL PRIMARY KEY,
    job_id INT NOT NULL REFERENCES jobs(id) ON DELETE CASCADE,
    locked_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    locked_by TEXT NOT NULL
);

CREATE INDEX idx_job_locks_job_id ON job_locks (job_id);

CREATE INDEX idx_holds_seat_status ON holds (seat_id, status);
CREATE INDEX idx_holds_expires_at ON holds (expires_at) WHERE status = 'active';
CREATE INDEX idx_bookings_user_id ON bookings (user_id);



-- Background worker dequeue index
-- Helps workers quickly find the next job that is ready to run.
-- Optimizes queries filtering by status='pending' and run_at.
-- Prevents full table scans as the jobs table grows.


-- Job Locks
-- Tracks which worker has currently locked a job.
-- Prevents multiple workers from processing the same job.
-- Mainly used for debugging and monitoring job execution.

-- Stores the timestamp when the job was locked.
-- Useful for detecting stuck or long-running jobs.

-- Stores the worker currently processing the job.
-- Helps identify which worker owns a lock.


-- Job Lock Lookup Index
-- Speeds up searches using job_id.
-- Quickly checks whether a job is already locked.
-- Avoids scanning the entire job_locks table.


-- Seat Hold Lookup Index
-- Quickly checks whether a seat already has an active hold.
-- Used during booking before creating a new hold.
-- Optimizes searches by seat_id and status.

-- Hold Expiry Index
-- Partial index containing only active holds.
-- Helps workers quickly find holds that have expired.
-- Ignores expired and confirmed holds for better performance.

-- User Booking Lookup Index
-- Speeds up fetching all bookings of a particular user.
-- Used when displaying booking history.
-- Prevents full table scans on the bookings table.
