import telebot
from telebot import types
import sqlite3

TOKEN = "8788796273:AAGau7lD_hI7hOo7vc9-UjfaIS9fFy1ZN6o"
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

# ==========================
# القائمة الرئيسية
# ==========================

def main_menu():

    markup = types.InlineKeyboardMarkup(row_width=2)

    markup.add(
        types.InlineKeyboardButton("🛒 شراء أرقام وهمية", callback_data="numbers")
    )

    markup.add(
        types.InlineKeyboardButton("📈 قسم الرشق", callback_data="smm")
    )

    markup.add(
        types.InlineKeyboardButton("💳 اشحن حسابك", callback_data="payment"),
        types.InlineKeyboardButton("🔗 رابط الدعوة", callback_data="ref")
    )

    markup.add(
        types.InlineKeyboardButton("⚙️ الإعدادات", callback_data="settings"),
        types.InlineKeyboardButton("🛠 الدعم الفني", callback_data="support")
    )

    return markup

# ==========================
# /start
# ==========================

@bot.message_handler(commands=["start"])
def start(message):

    add_user(message.from_user.id)

    balance = get_balance(message.from_user.id)

    bot.send_message(
        message.chat.id,
        f"""👋 أهلاً بك في بوت SULTAN PRO 👑

💰 رصيدك الحالي: {balance} ₽

اختر الخدمة من القائمة.""",
        reply_markup=main_menu()
    )

# ==========================
# الأزرار
# ==========================

@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):

    # شراء الأرقام
    if call.data == "numbers":

        markup = types.InlineKeyboardMarkup(row_width=2)

        markup.add(
            types.InlineKeyboardButton("📲 تيليجرام", callback_data="telegram"),
            types.InlineKeyboardButton("🟢 واتساب", callback_data="whatsapp")
        )

        markup.add(
            types.InlineKeyboardButton("🔙 رجوع", callback_data="home")
        )

        bot.edit_message_text(
            "🛒 شراء أرقام وهمية\n\nاختر الخدمة:",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=markup
        )

    # تيليجرام
    elif call.data == "telegram":

        markup = types.InlineKeyboardMarkup(row_width=2)

        markup.add(
            types.InlineKeyboardButton("🇪🇬 مصر - 20.5 ₽", callback_data="eg"),
            types.InlineKeyboardButton("🇺🇸 أمريكا - 17 ₽", callback_data="us")
        )

        markup.add(
            types.InlineKeyboardButton("🇸🇦 السعودية - 47.5 ₽", callback_data="sa"),
            types.InlineKeyboardButton("🇬🇧 بريطانيا - 26 ₽", callback_data="uk")
        )

        markup.add(
            types.InlineKeyboardButton("➡️ الصفحة 2", callback_data="telegram_page2")
        )

        markup.add(
            types.InlineKeyboardButton("🔙 رجوع", callback_data="numbers")
        )

        bot.edit_message_text(
            "📲 شراء أرقام تيليجرام\n\nاختر الدولة:",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=markup
        )

    # الرجوع للرئيسية
    elif call.data == "home":

        balance = get_balance(call.from_user.id)

        bot.edit_message_text(
            f"""👋 أهلاً بك في بوت SULTAN PRO 👑

💰 رصيدك الحالي: {balance} ₽

اختر الخدمة من القائمة.""",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=main_menu()
        )

bot.infinity_polling()
