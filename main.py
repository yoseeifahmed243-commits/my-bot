import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from sms import sms_menu
from countries import countries_menu

from config import TOKEN, BOT_NAME, SUPPORT
import database

bot = telebot.TeleBot(TOKEN)


# القائمة الرئيسية
def main_menu():
    markup = InlineKeyboardMarkup(row_width=2)

    markup.add(
        InlineKeyboardButton("📱 شراء أرقام SMS", callback_data="sms"),
        InlineKeyboardButton("📈 خدمات الرشق", callback_data="smm")
    )

    markup.add(
        InlineKeyboardButton("💳 شحن الرصيد", callback_data="deposit"),
        InlineKeyboardButton("👤 حسابي", callback_data="account")
    )

    markup.add(
        InlineKeyboardButton("🎁 الإحالة", callback_data="referral"),
        InlineKeyboardButton("📞 الدعم", url=f"https://t.me/{SUPPORT.replace('@','')}")
    )

    return markup


@bot.message_handler(commands=['start'])
def start(message):
    database.add_user(message.from_user.id)

    balance = database.get_balance(message.from_user.id)

    text = f"""
✨ أهلاً بك في {BOT_NAME}

💰 رصيدك الحالي: {balance}$

اختر الخدمة من القائمة بالأسفل.
"""

    bot.send_message(
        message.chat.id,
        text,
        reply_markup=main_menu()
    )


@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):

    if call.data == "sms":
        bot.edit_message_text(
            "📱 اختر الخدمة",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=sms_menu()
        )

    elif call.data.startswith("sms_"):
        service = call.data.replace("sms_", "")

        bot.edit_message_text(
            "🌍 اختر الدولة",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=countries_menu(service)
        )

    elif call.data.startswith("buy_"):
        _, service, country = call.data.split("_", 2)

        bot.answer_callback_query(call.id)

        bot.send_message(
            call.message.chat.id,
            f"""✅ الخدمة: {service}

🌍 الدولة: {country}

⏳ جاري شراء الرقم..."""
        )

    elif call.data == "smm":
        bot.answer_callback_query(call.id)
        bot.send_message(
            call.message.chat.id,
            "📈 قسم خدمات الرشق (قريبًا)."
        )

    elif call.data == "deposit":
        bot.answer_callback_query(call.id)
        bot.send_message(
            call.message.chat.id,
            "💳 قسم شحن الرصيد (قريبًا)."
        )

    elif call.data == "account":
        balance = database.get_balance(call.from_user.id)

        bot.send_message(
            call.message.chat.id,
            f"👤 حسابك\n\n💰 الرصيد: {balance}$"
        )

    elif call.data == "referral":
        bot.send_message(
            call.message.chat.id,
            "🎁 نظام الإحالة (قريبًا)."
        )


print("Bot Started...")
bot.infinity_polling()
