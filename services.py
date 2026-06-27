# services.py

# سعر الدولار = 20 روبل
USD_RATE = 20

# نسبة الربح
PROFIT_PERCENT = 30


def calc_price(rub_price):
    """
    يحول السعر من الروبل إلى الدولار
    ثم يضيف نسبة الربح
    """
    usd = rub_price / USD_RATE
    final_price = usd * (1 + PROFIT_PERCENT / 100)
    return round(final_price, 2)


# الخدمات (سعر المورد بالروبل)
SERVICES = {
    "telegram": {
        "name": "📲 Telegram",
        "rub_price": 20
    },
    "whatsapp": {
        "name": "🟢 WhatsApp",
        "rub_price": 25
    },
    "instagram": {
        "name": "📸 Instagram",
        "rub_price": 30
    },
    "tiktok": {
        "name": "🎵 TikTok",
        "rub_price": 35
    },
    "google": {
        "name": "🔵 Google",
        "rub_price": 20
    },
    "apple": {
        "name": "🍎 Apple",
        "rub_price": 45
    },
    "paypal": {
        "name": "💙 PayPal",
        "rub_price": 60
    }
}# services.py

# سعر الدولار = 20 روبل
USD_RATE = 20

# نسبة الربح
PROFIT_PERCENT = 30


def calc_price(rub_price):
    """
    يحول السعر من الروبل إلى الدولار
    ثم يضيف نسبة الربح
    """
    usd = rub_price / USD_RATE
    final_price = usd * (1 + PROFIT_PERCENT / 100)
    return round(final_price, 2)


# الخدمات (سعر المورد بالروبل)
SERVICES = {
    "telegram": {
        "name": "📲 Telegram",
        "rub_price": 20
    },
    "whatsapp": {
        "name": "🟢 WhatsApp",
        "rub_price": 25
    },
    "instagram": {
        "name": "📸 Instagram",
        "rub_price": 30
    },
    "tiktok": {
        "name": "🎵 TikTok",
        "rub_price": 35
    },
    "google": {
        "name": "🔵 Google",
        "rub_price": 20
    },
    "apple": {
        "name": "🍎 Apple",
        "rub_price": 45
    },
    "paypal": {
        "name": "💙 PayPal",
        "rub_price": 60
    }
}
