import telebot
from telebot import types
import sqlite3

API_TOKEN = "8788796273:AAFeq08ENxml7Afo_rz0LFDXTxAg1ukZQ78"
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
        types.InlineKeyboardButton("🛒 شراء أرقام وهمية", callback_data="buy_numbers"),
        types.InlineKeyboardButton("📈 قسم الرشق", callback_data="smm")
    )

    markup.add(
        types.InlineKeyboardButton("💳 اشحن حسابك", callback_data="payment"),
        types.InlineKeyboardButton("🔗 رابط الدعوة", callback_data="referral")
    )

    markup.add(
        types.InlineKeyboardButton("⚙️ الإعدادات", callback_data="settings"),
        types.InlineKeyboardButton("🛠 الدعم الفني", callback_data="support")
    )

    return markup

    return markup

# =====================
# ستارت
# =====================

@bot.message_handler(commands=['start'])
@bot.message_handler(commands=['start'])
def start(message):

    add_user(message.from_user.id)

    balance = get_balance(message.from_user.id)

    bot.send_message(
        message.chat.id,
        f"""👋 أهلاً بك في بوت SULTAN PRO 👑

✨ نقدم لك أفضل خدمات الأرقام الوهمية والرشق.

💰 رصيدك الحالي: {balance} ₽

اختر الخدمة من الأزرار بالأسفل.""",
        reply_markup=main_menu()
    )

# =====================
# تشغيل البوت
# =====================
# =====================
# الأزرار
# =====================

@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):

    # شراء أرقام وهمية
    if call.data == "buy_numbers":

        markup = types.InlineKeyboardMarkup(row_width=2)

        markup.add(
            types.InlineKeyboardButton("📲 تيليجرام", callback_data="telegram_numbers"),
            types.InlineKeyboardButton("🟢 واتساب", callback_data="whatsapp_numbers")
        )

        markup.add(
            types.InlineKeyboardButton("🔙 رجوع", callback_data="back_main")
        )

        bot.edit_message_text(
            "🛒 شراء أرقام وهمية\n\nاختر الخدمة المطلوبة:",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=markup
        )

    # رجوع للرئيسية
    elif call.data == "back_main":

        balance = get_balance(call.from_user.id)

        bot.edit_message_text(
            f"""👋 أهلاً بك في بوت SULTAN PRO 👑

✨ نقدم لك أفضل خدمات الأرقام الوهمية والرشق.

💰 رصيدك الحالي: {balance} ₽

اختر الخدمة من الأزرار بالأسفل.""",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=main_menu()
)
bot.infinity_polling()
