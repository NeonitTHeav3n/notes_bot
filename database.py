import sqlite3
from datetime import datetime



def connect():
    return sqlite3.connect("notes.db")

def create_table():
    
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXIST notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL
            text TEXT NOT NULL,
            category TEXT,
            created_at TEXT NOT NULL
        )
    """)
    
    
    conn.commit()
    conn.close()

def add_note(user_id: int, text: str, category: str):
    conn = connect()
    cursor = conn.cursor()
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    cursor.execute(
        "INSERT INTO notes (user_id, text, category, created_at) VALUES (?, ?, ?, ?)",
        (user_id, text, category, now)
    )

    conn.commit()
    conn.close()

def get_all_notes(user_id: int):
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT * FROM notes WHERE user_id = ? ORDER BY id",
        (user_id,)
    )


    notes = cursor.fetchall()
    conn.close()
    return notes


def get_notes_by_id(user_id: int, note_id: int):
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT * FROM notes WHERE id = ? AND user_id = ?",
        (note_id, user_id)
    )
    
    note = cursor.fetchone()
    conn.close()
    return note

def delete_note(user_id: int, note_id: int):
    conn = connect()
    cursor = conn.cursor()

    
    cursor.execute(
        "SELECT * FROM notes WHERE id = ? AND user_id = ?",
        (note_id, user_id)
    )
    
    note = cursor.fetchone()
    
    if note is None:
        conn.close()
        return False
    
    cursor.execute(
        "DELETE FROM notes WHERE id = ? AND user_id = ?",
        (note_id, user_id)
    )

    conn.commit()
    conn.close()
    return True



def get_notes_by_category(user_id: int, category: str):
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT * FROM notes WHERE user_id = ? AND LOWER(category) = LOWER(?) ORDER BY id",
        (user_id, category)
    )
    
    notes = cursor.fetchall()
    conn.close()
    return notes

def get_categories(user_id: int):
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT DISTINCT category FROM notes WHERE user_id = ? AND category IS NOT NULL",
        (user_id,)
    )
    
    categories = [row[0] for row in cursor.fetchall() if row[0] is not None]
    conn.close()
    return categories



    























