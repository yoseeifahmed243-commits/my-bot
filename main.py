import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import (TOKEN, BOT_NAME, SUPPORT, ADMIN_ID, TON_ADDRESS, 
                    TRC20_ADDRESS, ERC20_ADDRESS, BEP20_ADDRESS, 
                    POLYGON_ADDRESS, FAUCETPAY, CWALLET)
import database
from sms import sms_menu
from countries import countries_menu
from deposit import deposit_menu
from admin import admin_menu, is_admin

bot = telebot.TeleBot(TOKEN)

# القائمة الرئيسية
def main_menu():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("📱 شراء أرقام SMS", callback_data="sms"),
        InlineKeyboardButton("💳 شحن الرصيد", callback_data="deposit")
    )
    markup.add(
        InlineKeyboardButton("👤 حسابي", callback_data="account"),
        InlineKeyboardButton("🔗 رابط الدعوة", callback_data="referral_link")
    )
    markup.add(
        InlineKeyboardButton("📞 الدعم", url=f"https://t.me/{SUPPORT.replace('@','')}")
    )
    return markup

# أمر Start مع إشعار للأدمن عند دخول مستخدم جديد
@bot.message_handler(commands=["start"])
def start(message):
    # إضافة المستخدم وإرسال إشعار إذا كان جديداً
    user_id = message.from_user.id
    new_user = database.add_user(user_id) # تأكد أن دالة add_user تعيد True إذا كان جديداً
    
    if new_user:
        bot.send_message(
            ADMIN_ID,
            f"🔔 مستخدم جديد انضم للبوت!\n\n👤 الاسم: {message.from_user.first_name}\n🆔 ID: {user_id}"
        )

    balance = database.get_balance(user_id)
    bot.send_message(message.chat.id, f"✨ أهلاً بك في {BOT_NAME}\n\n💰 رصيدك: {balance}$\n\nاختر الخدمة من الأسفل.", reply_markup=main_menu())

@bot.message_handler(commands=["admin"])
def admin(message):
    if is_admin(message.from_user.id):
        bot.send_message(message.chat.id, "👑 لوحة الأدمن", reply_markup=admin_menu())

# التعامل مع الأزرار (Callbacks)
@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):
    if call.data == "home":
        bot.edit_message_text("🏠 القائمة الرئيسية", call.message.chat.id, call.message.message_id, reply_markup=main_menu())
    
    elif call.data == "sms":
        bot.edit_message_text("📱 اختر الخدمة", call.message.chat.id, call.message.message_id, reply_markup=sms_menu())
    
    elif call.data.startswith("sms_"):
        service = call.data.replace("sms_", "")
        bot.edit_message_text("🌍 اختر الدولة", call.message.chat.id, call.message.message_id, reply_markup=countries_menu(service))
    
    elif call.data == "deposit":
        bot.edit_message_text("💳 اختر طريقة الشحن", call.message.chat.id, call.message.message_id, reply_markup=deposit_menu())
    
    elif call.data.startswith("pay_"):
        method = call.data.replace("pay_", "")
        addresses = {"ton": TON_ADDRESS, "trc20": TRC20_ADDRESS, "erc20": ERC20_ADDRESS, 
                     "bep20": BEP20_ADDRESS, "polygon": POLYGON_ADDRESS, "faucetpay": FAUCETPAY, "cwallet": CWALLET}
        
        bot.edit_message_text(f"💳 الدفع بواسطة: {method.upper()}\n\n📍 العنوان:\n`{addresses.get(method, 'غير متوفر')}`\n\n📸 أرسل صورة التحويل والمبلغ.", 
                              call.message.chat.id, call.message.message_id, parse_mode="Markdown",
                              reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("⬅️ رجوع", callback_data="deposit")))

    elif call.data == "referral_link":
        bot_username = bot.get_me().username
        referral_url = f"https://t.me/{bot_username}?start={call.from_user.id}"
        bot.edit_message_text(f"🔗 رابط الدعوة الخاص بك:\n\n{referral_url}\n\nشارك الرابط واربح مكافآت!", call.message.chat.id, call.message.message_id,
                              reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("⬅️ رجوع", callback_data="home")))

    elif call.data == "account":
        balance = database.get_balance(call.from_user.id)
        bot.answer_callback_query(call.id, f"رصيدك الحالي: {balance}$", show_alert=True)

# استقبال صور التحويل
@bot.message_handler(content_types=["photo"])
def receive_photo(message):
    bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "✅ تم استلام طلبك. سيتم التواصل معك قريباً.")

bot.infinity_polling()
