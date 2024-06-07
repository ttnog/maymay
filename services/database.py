import sqlite3

con = sqlite3.connect('services/crud_python.db', check_same_thread=False)
cursor = con.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliData TEXT NOT NULL,
        cliComeu TEXT NOT NULL,
        cliMood INTEGER,
        cliFofoca TEXT
    )
""")
con.commit()