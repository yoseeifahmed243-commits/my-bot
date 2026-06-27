from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def sms_menu():

    markup = InlineKeyboardMarkup(row_width=2)

    markup.add(
        InlineKeyboardButton("📲 Telegram", callback_data="sms_telegram")
    )

    markup.add(
        InlineKeyboardButton("🟢 WhatsApp", callback_data="sms_whatsapp")
    )

    markup.add(
        InlineKeyboardButton("⬅️ رجوع", callback_data="home")
    )

    return markup
