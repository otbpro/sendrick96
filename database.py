import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("otb_farmers.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS farmers (
        wa_id TEXT PRIMARY KEY, district TEXT, crop TEXT, created TEXT, last_active TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY, wa_id TEXT, message TEXT, reply TEXT, timestamp TEXT, csat INTEGER)''')
    conn.commit()
    return conn

def save_profile(wa_id, district, crop):
    conn = init_db()
    conn.execute("INSERT OR REPLACE INTO farmers VALUES (?, ?, ?, ?, ?)",
                 (wa_id, district, crop, datetime.now().isoformat(), datetime.now().isoformat()))
    conn.commit()

def get_profile(wa_id):
    conn = init_db()
    return conn.execute("SELECT district, crop FROM farmers WHERE wa_id=?", (wa_id,)).fetchone()

def log_conversation(wa_id, msg, reply, csat=None):
    conn = init_db()
    conn.execute("INSERT INTO history (wa_id, message, reply, timestamp, csat) VALUES (?,?,?,?,?)",
                 (wa_id, msg, reply, datetime.now().isoformat(), csat))
    conn.commit()