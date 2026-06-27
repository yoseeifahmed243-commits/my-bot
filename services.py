from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def countries_menu():
    markup = InlineKeyboardMarkup(row_width=2)

    countries = [
        ("🇺🇿 Uzbekistan - 25.5₽", "uzbekistan"),
        ("🇧🇩 Bangladesh - 12₽", "bangladesh"),
        ("🇸🇦 Saudi Arabia - 43.5₽", "saudi"),
        ("🇮🇹 Italy - 36.5₽", "italy"),
        ("🇲🇽 Mexico - 22₽", "mexico"),
        ("🇰🇿 Kazakhstan - 33₽", "kazakhstan"),
        ("🇾🇪 Yemen - 20₽", "yemen"),
        ("🇱🇻 Latvia - 51₽", "latvia"),
        ("🇵🇹 Portugal - 65.5₽", "portugal"),
        ("🇰🇬 Kyrgyzstan - 43.5₽", "kyrgyzstan"),
        ("🇹🇯 Tajikistan - 25.5₽", "tajikistan"),
        ("🇺🇸 United States - 13₽", "usa"),
        ("🇪🇬 Egypt - 16.5₽", "egypt"),
        ("🇮🇶 Iraq - 65.5₽", "iraq"),
        ("🇹🇷 Turkey - 36.5₽", "turkey"),
        ("🇻🇪 Venezuela - 36.5₽", "venezuela"),
        ("🇨🇴 Colombia - 12₽", "colombia"),
        ("🇿🇼 Zimbabwe - 13₽", "zimbabwe"),
    ]

    for text, code in countries:
        markup.add(
            InlineKeyboardButton(
                text,
                callback_data=f"buy_{code}"
            )
        )

    markup.add(
        InlineKeyboardButton("⬅️ رجوع", callback_data="sms")
    )

    return markup
