# sqlite_setup.py
import sqlite3

# Connect to SQLite database (create one if not exists)
conn = sqlite3.connect('word_data.db')

# Create a table to store data
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS daily_words (
        date TEXT PRIMARY KEY,
        word TEXT,
        definition TEXT,
        example1 TEXT,
        example2 TEXT
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
