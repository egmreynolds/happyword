import sqlite3

def insert_word_into_sqlite(date, word, definition, example1, example2):
    conn = sqlite3.connect('word_data.db')
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO daily_words (date, word, definition, example1, example2) VALUES (?, ?, ?, ?, ?)",
        (date, word, definition, example1, example2)
    )

    conn.commit()
    conn.close()
    
    
insert_word_into_sqlite("02/01/2024", "happy", "the meaning of life", "Eg: I'm happy", "Eg: Be happy")