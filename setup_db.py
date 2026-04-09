import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER,
    name TEXT,
    total_spent INTEGER
)
""")

cursor.execute("""
INSERT INTO customers VALUES
(1, 'Alice', 1200),
(2, 'Bob', 800),
(3, 'Charlie', 1500)
""")

conn.commit()
conn.close()
