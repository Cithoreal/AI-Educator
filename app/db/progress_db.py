#ChatGPT generated file as part of project setup
import sqlite3
import os

DB_PATH = "data/edu_progress.db"

def init_db():
    
    db_dir = os.path.dirname(DB_PATH)
    print(db_dir)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir, exist_ok=True)
        
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lesson_title TEXT,
            date_completed TEXT,
            quiz_score INTEGER,
            notes TEXT
        )
    ''')
    
    conn.commit()
    conn.close()
    
def log_progress(title, date, score, notes):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
                   INSERT INTO progress (lesson_title, date_completed, quiz_score, notes)
                   Values (?, ?, ?, ?)
                   ''', (title, date, score, notes))
    conn.commit()
    conn.close()