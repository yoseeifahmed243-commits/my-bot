import telebot
from telebot import types
import sqlite3

# ==========================
# الإعدادات
# ==========================

TOKEN = "8788796273:AAHEarmEVW_kemB5kBTFwi9bqARewAyf3DM"
ADMIN_ID = 8767607098

bot = telebot.TeleBot(TOKEN)

# ==========================
# قاعدة البيانات
# ==========================

db = sqlite3.connect("bot.db", check_same_thread=False)
cur = db.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    balance REAL DEFAULT 0
)
""")

db.commit()

# ==========================
# الدوال
# ==========================

def add_user(user_id):
    cur.execute(
        "INSERT OR IGNORE INTO users(user_id) VALUES(?)",
        (user_id,)
    )
    db.commit()

def get_balance(user_id):
    cur.execute(
        "SELECT balance FROM users WHERE user_id=?",
        (user_id,)
    )
    row = cur.fetchone()

    if row:
        return row[0]

    return 0
