from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def sms_menu():

    markup = InlineKeyboardMarkup(row_width=2)

    markup.add(
        InlineKeyboardButton("📲 Telegram", callback_data="sms_telegram"),
        InlineKeyboardButton("🟢 WhatsApp", callback_data="sms_whatsapp")
    )

    markup.add(
        InlineKeyboardButton("📸 Instagram", callback_data="sms_instagram"),
        InlineKeyboardButton("🎵 TikTok", callback_data="sms_tiktok")
    )

    markup.add(
        InlineKeyboardButton("🔵 Google", callback_data="sms_google"),
        InlineKeyboardButton("🍎 Apple", callback_data="sms_apple")
    )

    markup.add(
        InlineKeyboardButton("💙 PayPal", callback_data="sms_paypal")
    )

    markup.add(
        InlineKeyboardButton("⬅️ رجوع", callback_data="home")
    )

    return markup
