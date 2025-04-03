import sqlite3

conn = sqlite3.connect("mistakes.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM mistakes")
rows = cursor.fetchall()

for row in rows:
    print(row)  # Print all stored mistakes

conn.close()
