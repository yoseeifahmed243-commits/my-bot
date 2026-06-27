import telebot
from telebot import types

# ضع التوكن الجديد هنا
API_TOKEN = '8788796273:AAHO_IpxG8rDg2nDzFtq8Ifxs5kmPFVud_k'
ADMIN_ID =  8767607098 # ضع الـ ID الخاص بك هنا

bot = telebot.TeleBot(API_TOKEN)

# قائمة دول وهمية (يمكنك التعديل عليها)
raw_countries = [("Uzbekistan", 25.5), ("Bangladesh", 12), ("Saudi Arabia", 43.5), 
                 ("Italy", 36.5), ("Mexico", 22), ("Kazakhstan", 33), 
                 ("Yemen", 20), ("Latvia", 51)]

def get_countries_with_markup(page=1):
    markup = types.InlineKeyboardMarkup(row_width=2)
    # إضافة زيادة 30%
    for name, price in raw_countries:
        new_price = round(price * 1.3, 1)
        markup.add(types.InlineKeyboardButton(f"{name} : {new_price} P", callback_data=f"buy_{name}"))
    
    # صفحة التنقل
    markup.row(*[types.InlineKeyboardButton(str(i), callback_data=f"page_{i}") for i in range(1, 5)])
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="main_menu"))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("🤍 شراء أرقام وهمية 🤍", "💙 قسم الرشق وزيادة المتابعين 💙", "🤍 الدعم الفني 🤍")
    
    text = (
        "🤍 اهلا بك عزيزي : Telegram SMS 🤍\n"
        "🕌 في القائمة الرئيسية لدى بوت السلطان 🕌\n"
        "-------------------------------------\n"
        f"👤 أيدي الحساب : {message.from_user.id}\n"
        "💰 رصيد حسابك الان : P 0 💰\n"
        "⬇️ اتحكم بالبوت من خلال الازرار بالأسفل ⬇️"
    )
    bot.send_message(message.chat.id, text, reply_markup=markup)

# --- قسم الأرقام ---
@bot.message_handler(func=lambda message: message.text == "🤍 شراء أرقام وهمية 🤍")
def buy_numbers(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    services = ["واتساب", "تيليجرام", "فيسبوك", "تيك توك", "انستجرام"]
    for s in services:
        markup.add(types.InlineKeyboardButton(s, callback_data=f"type_{s}"))
    bot.send_message(message.chat.id, "✅ اختر المنصة:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("type_"))
def show_countries(call):
    bot.edit_message_text("✅ اختر الدولة:", call.message.chat.id, call.message.message_id, reply_markup=get_countries_with_markup())

# --- قسم الرشق ---
@bot.message_handler(func=lambda message: message.text == "💙 قسم الرشق وزيادة المتابعين 💙")
def reshaq_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    services = ["انستجرام", "تيك توك", "فيسبوك", "تيليجرام", "واتساب"]
    for s in services:
        markup.add(types.InlineKeyboardButton(f"💙 {s}", callback_data=f"reshaq_{s}"))
    bot.send_message(message.chat.id, "💙 اختر منصة الرشق:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("reshaq_"))
def ask_link(call):
    platform = call.data.split("_")[1]
    msg = bot.send_message(call.message.chat.id, f"✅ تم اختيار {platform}\nأرسل الرابط الآن:")
    bot.register_next_step_handler(msg, lambda m: finalize(m, platform))

def finalize(message, platform):
    bot.send_message(ADMIN_ID, f"🚀 طلب جديد: {platform}\n👤 المستخدم: @{message.from_user.username}\n🔗 الرابط: {message.text}")
    bot.reply_to(message, "تم استلام طلبك.")

bot.polling(none_stop=True)
