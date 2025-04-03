import sqlite3

# Initialize database
def init_db():
    conn = sqlite3.connect("mistakes.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mistakes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_input TEXT,
            correct_response TEXT,
            explanation TEXT
        )
    """)
    conn.commit()
    conn.close()

# Store mistake in database
def store_mistake(user_input, correct_response, explanation):
    conn = sqlite3.connect("mistakes.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO mistakes (user_input, correct_response, explanation) VALUES (?, ?, ?)", 
                   (user_input, correct_response, explanation))
    conn.commit()
    conn.close()

# Retrieve mistakes for summary
def get_mistakes():
    conn = sqlite3.connect("mistakes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT user_input, correct_response, explanation FROM mistakes")
    mistakes = cursor.fetchall()
    conn.close()
    return mistakes

# ✅ Clear all mistakes from database
def clear_mistakes():
    conn = sqlite3.connect("mistakes.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM mistakes")
    conn.commit()
    conn.close()
