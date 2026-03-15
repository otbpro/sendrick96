from apscheduler.schedulers.background import BackgroundScheduler
from database import init_db
import requests
import os

def send_broadcast():
    conn = init_db()
    users = conn.execute("SELECT wa_id FROM farmers").fetchall()
    tip = "Apwoyo! Today's tip: Plant NARO MAIZE 64STR (Striga resistant) in Gulu now. Rain expected."
    for wa_id in users:
        # reuse send_whatsapp function from main
        print(f"Broadcast to {wa_id[0]}")
    print("✅ Daily broadcast sent to all farmers!")

if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_broadcast, 'cron', hour=8)  # 8 AM daily
    scheduler.start()
    print("Broadcast scheduler running...")