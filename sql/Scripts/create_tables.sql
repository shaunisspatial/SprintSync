CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
);

CREATE TABLE tasks (
    task_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    description TEXT NOT NULL,
    status VARCHAR(20) NOT NULL,
    estimated_hours FLOAT
);

CREATE TABLE time_entries (
    entry_id SERIAL PRIMARY KEY,
    task_id INT REFERENCES tasks(task_id),
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    duration INTERVAL
);

CREATE TABLE calendar_events (
    event_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    description TEXT
);
