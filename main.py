import telebot
from telebot import types

TOKEN = '8851361153:AAGhmCZJrEeAwC8JbA8l4ehyOUC6zBJe9hg'
bot = telebot.TeleBot(TOKEN)

# البيانات المعتمدة
SUPPORT_USER = "@elegramSMS_Support23"
CWALLET_ID = "61824874"
FAUCETPAY_USER = "TelegramSMS"

def get_back_button():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("✖️ رجوع للقائمة الرئيسية", callback_data="main"))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user
    text = (f"👋 اهلا بك عزيزي : {user.first_name}\n"
            f"♕ في القائمة الرئيسية لدى بوت السلطان ♕\n"
            f"-------------------------------\n"
            f"📧 حسابك : {user.id}@SULTAN.COM\n"
            f"💰 رصيد حسابك الان : 0 ₱\n"
            f"-------------------------------\n"
            f"⬇️ اتحكم بالبوت من خلال الازرار بالأسفل ⬇️")
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("♡ شراء أرقام وهمية (تليجرام/واتساب) ♡", callback_data="numbers"),
        types.InlineKeyboardButton("♡ قسم المتابعين والخدمات (رشق) ♡", callback_data="rashq"),
        types.InlineKeyboardButton("♡ شحن حسابك (طرق الدفع) ♡", callback_data="payment"),
        types.InlineKeyboardButton("♡ مشاركة رابط الدعوة الخاص بك ♡", callback_data="referral"),
        types.InlineKeyboardButton("♡ الدعم الفني ♡", url=f"https://t.me/{SUPPORT_USER.replace('@', '')}")
    )
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == "main":
        start(call.message)
        
    elif call.data == "numbers":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("📱 أرقام تليجرام", callback_data="n_tg"),
                   types.InlineKeyboardButton("📱 أرقام واتساب", callback_data="n_wa"),
                   types.InlineKeyboardButton("✖️ رجوع", callback_data="main"))
        bot.edit_message_text("📱 قسم شراء الأرقام الوهمية:", call.message.chat.id, call.message.message_id, reply_markup=markup)
        
    elif call.data == "rashq":
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("فيسبوك", callback_data="r_fb"),
                   types.InlineKeyboardButton("إنستجرام", callback_data="r_insta"),
                   types.InlineKeyboardButton("تليجرام", callback_data="r_tg"),
                   types.InlineKeyboardButton("تيك توك", callback_data="r_tt"),
                   types.InlineKeyboardButton("جوجل", callback_data="r_go"),
                   types.InlineKeyboardButton("✖️ رجوع", callback_data="main"))
        bot.edit_message_text("📢 قسم المتابعين والخدمات (رشق):", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == "payment":
        text = (f"💳 طرق الدفع المتاحة للشحن:\n\n"
                f"• Cwallet ID: {CWALLET_ID}\n"
                f"• FaucetPay: {FAUCETPAY_USER}\n"
                f"• USDT (TRC-20, BEP-20, Polygon)\n"
                f"• عملات TON\n\n"
                f"⚠️ بعد التحويل أرسل صورة الإيصال للدعم: {SUPPORT_USER}")
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=get_back_button())

    elif call.data == "referral":
        bot.edit_message_text(f"🔗 رابط الدعوة الخاص بك:\nhttps://t.me/{(bot.get_me().username)}?start={call.message.chat.id}\n\nشارك الرابط واربح رصيداً مجانياً!", call.message.chat.id, call.message.message_id, reply_markup=get_back_button())

    elif call.data.startswith("n_") or call.data.startswith("r_"):
        bot.edit_message_text(f"✅ تم اختيار الخدمة. تواصل مع الدعم لإتمام الطلب فوراً:\n{SUPPORT_USER}", call.message.chat.id, call.message.message_id, reply_markup=get_back_button())

if __name__ == "__main__":
    bot.remove_webhook()
    bot.polling(none_stop=True)
