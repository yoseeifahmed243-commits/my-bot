import telebot
from telebot import types

API_TOKEN = 'YOUR_BOT_TOKEN_HERE'
bot = telebot.TeleBot(API_TOKEN)

# --- دوال حساب الربح ---
def add_fixed_profit(price):
    return round(float(price) + 5.0, 2)  # زيادة 5 روبل ثابتة للأرقام

def add_percent_profit(price):
    return round(float(price) * 1.05, 2) # زيادة 5% للرشق

# --- القائمة الرئيسية ---
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("📱 أرقام وهمية", callback_data="numbers_menu"),
        types.InlineKeyboardButton("📈 خدمات الرشق", callback_data="reshaq_menu"),
        types.InlineKeyboardButton("💳 شحن الرصيد", callback_data="payment_info"),
        types.InlineKeyboardButton("🎁 الإحالة", callback_data="referral_menu"),
        types.InlineKeyboardButton("🎧 الدعم", callback_data="support_menu")
    )
    bot.send_message(message.chat.id, "✨ **مرحباً بك في بوت السلطان**\n📊 رصيدك: 0 ₽", reply_markup=markup, parse_mode="Markdown")

# --- 1. قسم الأرقام (زيادة 5 روبل) ---
@bot.callback_query_handler(func=lambda call: call.data == "numbers_menu")
def numbers_menu(call):
    markup = types.InlineKeyboardMarkup(row_width=2)
    numbers = {"أوزبكستان": 25.5, "السعودية": 43.5, "مصر": 16.5, "العراق": 65.5}
    for country, price in numbers.items():
        markup.add(types.InlineKeyboardButton(f"{country} ({add_fixed_profit(price)} ₽)", callback_data=f"buy_{country}"))
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="start"))
    bot.edit_message_text("📱 **اختر الدولة (الأسعار شاملة الربح):**", call.message.chat.id, call.message.message_id, reply_markup=markup)

# --- 2. قسم الرشق (زيادة 5%) ---
@bot.callback_query_handler(func=lambda call: call.data == "reshaq_menu")
def reshaq_menu(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    services = {"متابعين انستا (1000)": 50.0, "لايكات انستا (1000)": 20.0}
    for service, price in services.items():
        markup.add(types.InlineKeyboardButton(f"{service} ({add_percent_profit(price)} ₽)", callback_data=f"buy_reshaq_{service}"))
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="start"))
    bot.edit_message_text("📈 **اختر خدمة الرشق:**", call.message.chat.id, call.message.message_id, reply_markup=markup)

# --- 3. الشحن التفاعلي (مطابق للصورة) ---
@bot.callback_query_handler(func=lambda call: call.data == "payment_info")
def payment_methods(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    methods = [("💙 FaucetPay", "pay_faucet"), ("🟢 CWallet", "pay_cwallet"), ("💎 TON", "pay_ton")]
    for text, cd in methods: markup.add(types.InlineKeyboardButton(text, callback_data=cd))
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="start"))
    bot.edit_message_text("💳 **اختر طريقة الشحن:**", call.message.chat.id, call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("pay_"))
def show_details(call):
    method = call.data.split("_")[1]
    details = {"faucet": "📧 `telegramsms71@gmail.com`", "cwallet": "💸 `61824874`", "ton": "💎 `UQBEejOP...`"}
    text = f"💳 **تفاصيل {method.upper()}**\n\n{details.get(method, '')}\n\n⚠️ بعد التحويل أرسل الإيصال للدعم."
    markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🎧 تواصل مع الدعم", url="https://t.me/elegramSMS_Support23"), types.InlineKeyboardButton("🔙 رجوع", callback_data="payment_info"))
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

# --- 4. باقي الأقسام ---
@bot.callback_query_handler(func=lambda call: call.data in ["support_menu", "referral_menu"])
def menu_extras(call):
    text = "🎧 **الدعم الفني:** @Sultan_Support27" if call.data == "support_menu" else "🎁 **رابط الإحالة:** ارسله لأصدقائك!"
    markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🔙 رجوع", callback_data="start"))
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)

bot.polling(none_stop=True)
