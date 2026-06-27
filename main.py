import telebot
from telebot import types

# 1. الإعدادات الأساسية
API_TOKEN = '8788796273:AAHO_IpxG8rDg2nDzFtq8Ifxs5kmPFVud_k' 
ADMIN_ID = 8788796273 
bot = telebot.TeleBot(API_TOKEN)

# دالة حساب السعر بزيادة 30%
def get_price(base_price):
    return round(base_price * 1.3, 2)

# 2. القائمة الرئيسية
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("💳 شحن الرصيد", callback_data="payment_info"),
        types.InlineKeyboardButton("📈 خدمات الرشق", callback_data="reshaq_menu"),
        types.InlineKeyboardButton("📱 شراء أرقام SMS", callback_data="numbers_menu"),
        types.InlineKeyboardButton("👤 حسابي", callback_data="profile"),
        types.InlineKeyboardButton("🎁 الإحالة", callback_data="referral_menu"),
        types.InlineKeyboardButton("🎧 الدعم", callback_data="support_menu")
    )
    welcome_text = (
        "✨ **أهلاً بك في بوت السلطان للخدمات الرقمية** ✨\n\n"
        "الخيار الأول للرشق، الأرقام، والخدمات السريعة.\n"
        "📊 رصيدك الحالي: 0 ₽"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode="Markdown")

# 3. نظام الشحن التفاعلي (مطابق للتصميم)
@bot.callback_query_handler(func=lambda call: call.data == "payment_info")
def payment_methods_menu(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    methods = [
        ("💙 FaucetPay", "pay_faucet"),
        ("🟢 CWallet", "pay_cwallet"),
        ("💎 TON", "pay_ton"),
        ("🟡 USDT BEP20", "pay_bep20"),
        ("🔵 USDT TRC20", "pay_trc20"),
        ("⚫ USDT ERC20", "pay_erc20"),
        ("🟣 USDT Polygon", "pay_polygon"),
        ("🔙 رجوع", "start")
    ]
    for text, callback in methods:
        markup.add(types.InlineKeyboardButton(text, callback_data=callback))
    bot.edit_message_text("💳 **اختر طريقة الشحن المناسبة:**", call.message.chat.id, call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("pay_"))
def show_wallet_details(call):
    method = call.data.split("_")[1]
    details = {
        "faucet": "📧 **FaucetPay**\n`telegramsms71@gmail.com`",
        "cwallet": "💸 **ID Cwallet**\n`61824874`",
        "ton": "💎 **TON**\n`UQBEejOPxeZK8DyVwkAVQznE1FrMi0EbxxJSia7MhS4H1Co7`",
        "bep20": "🟡 **USDT BEP20**\n`0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155`",
        "trc20": "🔵 **USDT TRC20**\n`TRHUB8kuMpdCoDzST6c4AJ4cJdk6tToz97`",
        "erc20": "⚫ **USDT ERC20**\n`0x8D7dDE7719e9d6D3e5175CE170Fae00372715493`",
        "polygon": "🟣 **USDT Polygon**\n`0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155`"
    }
    text = (f"💳 **طريقة الدفع:** {method.upper()}\n\n{details.get(method, '')}\n\n"
            "📥 حول المبلغ إلى عنوان هذه الشبكة.\n"
            "ثم اضغط إرسال صورة التحويل للدعم مع كتابة المبلغ.")
    markup = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton("🎧 تواصل مع الدعم لإثبات الدفع", url="https://t.me/elegramSMS_Support23"),
        types.InlineKeyboardButton("🔙 رجوع للقائمة", callback_data="payment_info")
    )
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

# 4. باقي الأقسام (الدعوة والدعم)
@bot.callback_query_handler(func=lambda call: call.data == "referral_menu")
def referral_menu(call):
    text = f"🎁 **نظام الإحالة**\nرابط دعوتك: https://t.me/YourBotName?start={call.from_user.id}"
    markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🔙 رجوع", callback_data="start"))
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "support_menu")
def support_menu(call):
    text = "🎧 **مركز الدعم الفني**\nتواصل معنا: @elegramSMS_Support23"
    markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🔙 رجوع", callback_data="start"))
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)

bot.polling(none_stop=True)
