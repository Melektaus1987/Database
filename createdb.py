import sqlite3
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

def create_users():
    conn = sqlite3.connect("users.db")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
       id INTEGER PRIMARY KEY,
       login TEXT NOT NULL,
       password NEXT NOT NULL
    )
    """
)

def add_users_into_databaise(login, password):
    cursor.execute("""
    INSERT INTO users (login, password) VALUES(?,?)""", (login, password))
    conn.commit()