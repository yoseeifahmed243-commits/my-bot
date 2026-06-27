from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

COUNTRIES = {

    "telegram": [
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
    ],

    "whatsapp": [
        ("🇵🇭 Philippines - 10₽", "philippines"),
        ("🇻🇳 Vietnam - 10₽", "vietnam"),
        ("🇮🇩 Indonesia - 10₽", "indonesia"),
        ("🇹🇭 Thailand - 10₽", "thailand"),
        ("🇨🇦 Canada - 10₽", "canada"),
        ("🇪🇬 Egypt - 10₽", "egypt"),
        ("🇿🇦 South Africa - 10₽", "southafrica"),
        ("🇲🇦 Morocco - 13₽", "morocco"),
        ("🇱🇾 Libya - 10₽", "libya"),
        ("🇫🇷 France - 10₽", "france"),
        ("🇸🇦 Saudi Arabia - 18₽", "saudi"),
        ("🇬🇧 United Kingdom - 10₽", "uk"),
        ("🇹🇷 Turkey - 10₽", "turkey"),
        ("🇮🇶 Iraq - 10₽", "iraq"),
    ],

    "instagram": [],
    "tiktok": []

}

def countries_menu(service):

    markup = InlineKeyboardMarkup(row_width=2)

    for text, code in COUNTRIES.get(service, []):

        markup.add(
            InlineKeyboardButton(
                text,
                callback_data=f"buy_{service}_{code}"
            )
        )

    markup.add(
        InlineKeyboardButton("⬅️ رجوع", callback_data="sms")
    )

    return markup
