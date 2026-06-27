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

    country = call.data.replace("buy_", "")

    prices = {
        "uzbekistan": 25.5,
        "bangladesh": 12,
        "saudi": 43.5,
        "italy": 36.5,
        "mexico": 22,
        "kazakhstan": 33,
        "yemen": 20,
        "latvia": 51,
        "portugal": 65.5,
        "kyrgyzstan": 43.5,
        "tajikistan": 25.5,
        "usa": 13,
        "egypt": 16.5,
        "iraq": 65.5,
        "turkey": 36.5,
        "venezuela": 36.5,
        "colombia": 12,
        "zimbabwe": 13
    }

    rub_price = prices[country]
    final_price = round(rub_price * 1.30, 2)

    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(
            f"🛒 شراء مقابل {final_price} ₽",
            callback_data=f"confirm_{country}"
        )
    )
    markup.add(
        InlineKeyboardButton("⬅️ رجوع", callback_data="sms_telegram")
    )

    bot.edit_message_text(
        f"""📲 Telegram

🌍 الدولة: {country}

💰 السعر: {final_price} ₽

اضغط شراء لإكمال الطلب.""",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup
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
