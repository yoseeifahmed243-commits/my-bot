import telebot
from telebot import types
import sqlite3

API_TOKEN = "8788796273:AAEypT5ZhFLNFyEGeccUfPtSIzNFcGnYjzA"
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
    balance REAL DEFAULT 0,
    invited_by INTEGER DEFAULT 0
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


def add_balance(user_id, amount):
    cur.execute(
        "UPDATE users SET balance = balance + ? WHERE user_id=?",
        (amount, user_id)
    )
    db.commit()
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
# أمر /start
# =====================

@bot.message_handler(commands=["start"])
def start(message):
    add_user(message.from_user.id)

    balance = get_balance(message.from_user.id)

    bot.send_message(
        message.chat.id,
        f"""👋 أهلاً بك في بوت SULTAN PRO
    telegram_pages = [
    telegram_page1,
    telegram_page2,
    telegram_page3,
    telegram_page4,
    telegram_page5,
    telegram_page6,
    telegram_page7,
    telegram_page8,
]

def show_telegram_page(chat_id, page):
    markup = types.InlineKeyboardMarkup(row_width=2)

    text = f"📲 أرقام تيليجرام\n\n📄 الصفحة {page+1}/{len(telegram_pages)}\n\n"

    for country, price in telegram_pages[page]:
        text += f"🌍 {country} - {price} ₽\n"

    if page > 0:
        markup.add(types.InlineKeyboardButton("⬅️ السابق", callback_data=f"page_{page-1}"))

    if page < len(telegram_pages) - 1:
        markup.add(types.InlineKeyboardButton("➡️ التالي", callback_data=f"page_{page+1}"))

    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back"))

    bot.send_message(chat_id, text, reply_markup=markup)
    @bot.callback_query_handler(func=lambda call: True)
def callback(call):

    if call.data == "telegram_numbers":
        show_telegram_page(call.message.chat.id, 0)

    elif call.data.startswith("page_"):
        page = int(call.data.split("_")[1])
        show_telegram_page(call.message.chat.id, page)

    elif call.data == "back":
        balance = get_balance(call.from_user.id)

        bot.send_message(
            call.message.chat.id,
            f"💰 رصيدك: {balance} ₽",
            reply_markup=main_menu()
    )
    # =====================
# تشغيل البوت
# =====================

bot.infinity_polling()
