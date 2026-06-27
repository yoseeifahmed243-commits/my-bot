import telebot
from telebot import types

TOKEN = '8851361153:AAGhmCZJrEeAwC8JbA8l4ehyOUC6zBJe9hg'
bot = telebot.TeleBot(TOKEN)

# --- دالة مساعدة لزيادة الأسعار 30% تلقائياً ---
def price(p):
    return f"{round(p * 1.3, 3)} ₱"

def get_main_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("♡ شراء أرقام وهمية ♡", callback_data="numbers"),
        types.InlineKeyboardButton("♡ شحن حسابك ♡", callback_data="payment"),
        types.InlineKeyboardButton("♡ قسم الرشق وزيادة المتابعين ♡", callback_data="rashq"),
        types.InlineKeyboardButton("♡ الدعم الفني ♡", callback_data="support")
    )
    return markup

# --- القائمة الرئيسية ---
@bot.message_handler(commands=['start'])
def start(message):
    text = (f"👋 اهلا بك عزيزي : {message.from_user.first_name}\n"
            f"♕ في القائمة الرئيسية لدى بوت السلطان ♕\n"
            f"-------------------------------\n"
            f"💰 رصيد حسابك الان : 0 ₱\n"
            f"⬇️ اختر الخدمة من الأزرار بالأسفل ⬇️")
    bot.send_message(message.chat.id, text, reply_markup=get_main_menu())

# --- معالجة الأزرار ---
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == "numbers":
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(
            types.InlineKeyboardButton(f"فيتنام ({price(10)})", callback_data="buy"),
            types.InlineKeyboardButton(f"مصر ({price(10)})", callback_data="buy"),
            types.InlineKeyboardButton(f"السعودية ({price(18)})", callback_data="buy"),
            types.InlineKeyboardButton("🔙 رجوع", callback_data="main")
        )
        bot.edit_message_text("📱 اختر الدولة للأرقام الوهمية:", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "rashq":
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(
            types.InlineKeyboardButton("🐦 تويتر", callback_data="serv_twitter"),
            types.InlineKeyboardButton("🎵 تيك توك", callback_data="serv_tiktok"),
            types.InlineKeyboardButton("📘 فيسبوك", callback_data="serv_fb"),
            types.InlineKeyboardButton("🔙 رجوع", callback_data="main")
        )
        bot.edit_message_text("📢 قسم الرشق، اختر المنصة:", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "serv_fb":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton(f"تعليقات عشوائية ({price(0.04)})", callback_data="buy"),
            types.InlineKeyboardButton(f"مشاركات ضمان ({price(0.04)})", callback_data="buy"),
            types.InlineKeyboardButton("🔙 رجوع", callback_data="rashq")
        )
        bot.edit_message_text("📘 خدمات فيسبوك:", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "payment":
        text = "💳 طرق الشحن: بينانس، فودافون كاش، USDT، TON.\nأرسل الإيصال للدعم فوراً."
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🔙 رجوع", callback_data="main")))

    elif call.data == "main":
        bot.edit_message_text("👋 القائمة الرئيسية:", call.message.chat.id, call.message.message_id, reply_markup=get_main_menu())

if __name__ == "__main__":
    bot.polling(none_stop=True)
