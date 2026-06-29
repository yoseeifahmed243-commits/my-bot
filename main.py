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

    elif call.data == "telegram":

    markup = types.InlineKeyboardMarkup(row_width=2)

    markup.add(
        types.InlineKeyboardButton("🇷🇺 روسيا | 13 ₽", callback_data="tg_ru"),
        types.InlineKeyboardButton("🎲 عشوائي | 15 ₽", callback_data="tg_random")
    )

    markup.add(
        types.InlineKeyboardButton("🇵🇭 الفلبين | 15 ₽", callback_data="tg_ph"),
        types.InlineKeyboardButton("🇻🇳 فيتنام | 15 ₽", callback_data="tg_vn")
    )

    markup.add(
        types.InlineKeyboardButton("🇮🇩 إندونيسيا | 15 ₽", callback_data="tg_id"),
        types.InlineKeyboardButton("🇲🇾 ماليزيا | 15 ₽", callback_data="tg_my")
    )

    markup.add(
        types.InlineKeyboardButton("🇹🇭 تايلاند | 15 ₽", callback_data="tg_th"),
        types.InlineKeyboardButton("🇰🇿 كازاخستان | 16 ₽", callback_data="tg_kz")
    )

    markup.add(
        types.InlineKeyboardButton("🇪🇪 إستونيا | 15 ₽", callback_data="tg_ee"),
        types.InlineKeyboardButton("🇬🇧 بريطانيا | 31 ₽", callback_data="tg_uk")
    )

    markup.add(
        types.InlineKeyboardButton("➡️ الصفحة 2", elif call.data == "telegram_page2":

    markup = types.InlineKeyboardMarkup(row_width=2)

    markup.add(
        types.InlineKeyboardButton("🇮🇳 الهند | 15 ₽", callback_data="tg_in"),
        types.InlineKeyboardButton("🇵🇰 باكستان | 15 ₽", callback_data="tg_pk")
    )

    markup.add(
        types.InlineKeyboardButton("🇧🇩 بنغلاديش | 15 ₽", callback_data="tg_bd"),
        types.InlineKeyboardButton("🇳🇵 نيبال | 15 ₽", callback_data="tg_np")
    )

    markup.add(
        types.InlineKeyboardButton("🇱🇰 سريلانكا | 15 ₽", callback_data="tg_lk"),
        types.InlineKeyboardButton("🇨🇳 الصين | 20 ₽", callback_data="tg_cn")
    )

    markup.add(
        types.InlineKeyboardButton("🇯🇵 اليابان | 25 ₽", callback_data="tg_jp"),
        types.InlineKeyboardButton("🇰🇷 كوريا الجنوبية | 25 ₽", callback_data="tg_kr")
    )

    markup.add(
        types.InlineKeyboardButton("⬅️ الصفحة 1", callback_data="telegram"),
        types.InlineKeyboardButton("➡️ الصفحة 3", elif call.data == "telegram_page3":

    markup = types.InlineKeyboardMarkup(row_width=2)

    markup.add(
        types.InlineKeyboardButton("🇪🇬 مصر | 25.5 ₽", callback_data="tg_eg"),
        types.InlineKeyboardButton("🇸🇦 السعودية | 52.5 ₽", callback_data="tg_sa")
    )

    markup.add(
        types.InlineKeyboardButton("🇦🇪 الإمارات | 34.5 ₽", callback_data="tg_ae"),
        types.InlineKeyboardButton("🇶🇦 قطر | 36 ₽", callback_data="tg_qa")
    )

    markup.add(
        types.InlineKeyboardButton("🇰🇼 الكويت | 30.5 ₽", callback_data="tg_kw"),
        types.InlineKeyboardButton("🇧🇭 البحرين | 29 ₽", callback_data="tg_bh")
    )

    markup.add(
        types.InlineKeyboardButton("🇴🇲 عمان | 31 ₽", callback_data="tg_om"),
        types.InlineKeyboardButton("🇯🇴 الأردن | 25 ₽", callback_data="tg_jo")
    )

    markup.add(
        types.InlineKeyboardButton("🇮🇶 العراق | 15 ₽", callback_data="tg_iq"),
        types.InlineKeyboardButton("🇱🇧 لبنان | 20 ₽", callback_data="tg_lb")
    )

    markup.add(
        types.InlineKeyboardButton("⬅️ الصفحة 2", callback_data="telegram_page2"),
        types.InlineKeyboardButton("➡️ الصفحة 4", callback_data="telegram_page4")
    )

    markup.add(
        types.InlineKeyboardButton("🔙 رجوع", callback_data="numbers")
    )

    bot.edit_message_text(
        "📲 شراء أرقام تيليجرام\n\nالصفحة الثالثة:",
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=markup
    )
    )

    markup.add(
        types.InlineKeyboardButton("🔙 رجوع", callback_data="numbers")
    )

    bot.edit_message_text(
        "📲 شراء أرقام تيليجرام\n\nالصفحة الثانية:",
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=markup
    )
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

    elif call.data == "whatsapp":
        bot.answer_callback_query(call.id, "🟢 سيتم إضافة قائمة واتساب")

    elif call.data == "smm":
        bot.answer_callback_query(call.id, "📈 سيتم إضافة قسم الرشق")

    elif call.data == "payment":
        bot.answer_callback_query(call.id, "💳 سيتم إضافة الشحن")

    elif call.data == "ref":
        bot.answer_callback_query(call.id, "🔗 سيتم إضافة رابط الدعوة")

    elif call.data == "settings":
        bot.answer_callback_query(call.id, "⚙️ سيتم إضافة الإعدادات")

    elif call.data == "support":
        bot.send_message(
            call.message.chat.id,
            "🛠 الدعم الفني:\n@sms2221bot"
        )
# ==========================
# تشغيل البوت
# ==========================

print("Bot Started...")
bot.infinity_polling(skip_pending=True)
