import telebot
from telebot import types
import sqlite3

API_TOKEN"8788796273:AAGRnTS4g3_o3WdaeiB-fMgv9oWhzoRyBw8"
ADMIN_ID = 8767607098

bot = telebot.TeleBot(API_TOKEN)

# =====================
# قاعدة البيانات
# =====================

db = sqlite3.connect("bot.db", check_same_thread=False)
cur = db.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    balance REAL DEFAULT 0
)
""")

db.commit()

# =====================
# دوال الرصيد
# =====================

def add_user(user_id):
    cur.execute(
        "INSERT OR IGNORE INTO users(user_id,balance) VALUES(?,?)",
        (user_id, 0)
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

# =====================
# القائمة الرئيسية
# =====================

def main_menu():

    markup = types.InlineKeyboardMarkup(row_width=2)

    markup.add(
        types.InlineKeyboardButton("📲 أرقام تيليجرام", callback_data="telegram_numbers"),
        types.InlineKeyboardButton("💬 أرقام واتساب", callback_data="whatsapp_numbers")
    )

    markup.add(
        types.InlineKeyboardButton("📈 خدمات الرشق", callback_data="reshaq")
    )

    markup.add(
        types.InlineKeyboardButton("💳 شحن الرصيد", callback_data="payment")
    )

    markup.add(
        types.InlineKeyboardButton("🎁 الإحالة", callback_data="referral"),
        types.InlineKeyboardButton("🎧 الدعم", callback_data="support")
    )

    return markup

# =====================
# ستارت
# =====================

@bot.message_handler(commands=['start'])
def start(message):

    add_user(message.from_user.id)

    balance = get_balance(message.from_user.id)

    bot.send_message(
        message.chat.id,
        f"✨ مرحباً بك في البوت\n\n💰 رصيدك: {balance} ₽",
        reply_markup=main_menu()
    )

# =====================
# تشغيل البوت
# =====================

bot.infinity_polling()
