CREATE TABLE IF NOT EXISTS accounts (
    account_id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_name TEXT,
    account_secret TEXT,
    creation_date TIMESTAMP
)