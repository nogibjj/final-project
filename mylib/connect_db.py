import sqlite3

def connect_db():
    conn = sqlite3.connect("pokedex.db")
    cursor = conn.cursor()
    return conn,cursor

def close_db(conn):
    conn.close()
    