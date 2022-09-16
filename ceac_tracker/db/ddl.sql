DROP TABLE IF EXISTS application;
DROP TABLE IF EXISTS history;

CREATE TABLE application(
    application_id TEXT PRIMARY KEY,
    location TEXT,
    case_created TEXT,
    notification_email TEXT
);
CREATE TABLE history(
    record_id INTEGER PRIMARY KEY,
    application_id TEXT,
    update_date TEXT,
    status TEXT,
    description TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP

);