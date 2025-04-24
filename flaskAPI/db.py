# flaskAPI/db.py
import sqlite3

def get_db():
    conn = sqlite3.connect('dropoflife.db')
    return conn