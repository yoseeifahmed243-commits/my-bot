import telebot
from telebot import types
import sqlite3

TOKEN = "8788796273:AAHEarmEVW_kemB5kBTFwi9bqARewAyf3DM"
ADMIN_ID = 8767607098

bot = telebot.TeleBot(TOKEN)

db = sqlite3.connect("bot.db", check_same_thread=False)
cur = db.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    balance REAL DEFAULT 0
)
""")

db.commit()


def add_user(user_id):
    cur.execute(
        "INSERT OR IGNORE INTO users(user_id) VALUES(?)",
        (user_id,)
    )
    db.commit()


def get_balance(user_id):
    cur.execute(
        "SELECT balance FROM users WHERE user_id=?",
        (user_id,)
    )
    row = cur.fetchone()
return row[0] if row else 0
def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)

    markup.add(
        types.InlineKeyboardButton("🛒 شراء أرقام وهمية", callback_data="numbers")
    )

    markup.add(
        types.InlineKeyboardButton("📈 قسم الرشق", callback_data="smm")
    )

    markup.add(
        types.InlineKeyboardButton("💳 اشحن حسابك", callback_data="payment"),
        types.InlineKeyboardButton("🔗 رابط الدعوة", callback_data="ref")
    )

    markup.add(
        types.InlineKeyboardButton("⚙️ الإعدادات", callback_data="settings"),
        types.InlineKeyboardButton("🛠 الدعم الفني", callback_data="support")
    )

    return markup


@bot.message_handler(commands=["start"])
def start(message):

    add_user(message.from_user.id)

    balance = get_balance(message.from_user.id)

    bot.send_message(
        message.chat.id,
        f"""👋 أهلاً بك في بوت SULTAN PRO 👑

💰 رصيدك الحالي: {balance} ₽

اختر الخدمة من القائمة.""",
        reply_markup=main_menu()
)
@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):
        if call.data == "numbers":

        markup = types.InlineKeyboardMarkup(row_width=2)

        markup.add(
            types.InlineKeyboardButton("📲 تيليجرام", callback_data="telegram"),
            types.InlineKeyboardButton("🟢 واتساب", callback_data="whatsapp")
        )

        markup.add(
            types.InlineKeyboardButton("🔙 رجوع", callback_data="home")
        )

        bot.edit_message_text(
            "🛒 شراء أرقام وهمية\n\nاختر الخدمة:",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=markup
)
        elif call.data == "home":

        balance = get_balance(call.from_user.id)

        bot.edit_message_text(
            f"""👋 أهلاً بك في بوت SULTAN PRO 👑

💰 رصيدك الحالي: {balance} ₽

اختر الخدمة من القائمة.""",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=main_menu()
    )
        elif call.data== "ttelegram:
    markup = types.InlineKeyboardMarkup(row_width=2)

markup.add(
    types.InlineKeyboardButton("🇺🇿 Uzbekistan : 30.5 ₽", callback_data="buy_uzbekistan"),
    types.InlineKeyboardButton("🇧🇩 Bangladesh : 17 ₽", callback_data="buy_bangladesh")
)

markup.add(
    types.InlineKeyboardButton("🇸🇦 Saudi Arabia : 48.5 ₽", callback_data="buy_saudi"),
    types.InlineKeyboardButton("🇷🇺 Russia : 56 ₽", callback_data="buy_russia")
)

markup.add(
    types.InlineKeyboardButton("🇮🇹 Italy : 41.5 ₽", callback_data="buy_italy"),
    types.InlineKeyboardButton("🇲🇽 Mexico : 27 ₽", callback_data="buy_mexico")
)

markup.add(
    types.InlineKeyboardButton("🇾🇪 Yemen : 25 ₽", callback_data="buy_yemen"),
    types.InlineKeyboardButton("🇱🇻 Latvia : 56 ₽", callback_data="buy_latvia")
)

markup.add(
    types.InlineKeyboardButton("🇵🇹 Portugal : 70.5 ₽", callback_data="buy_portugal"),
    types.InlineKeyboardButton("🇰🇬 Kyrgyzstan : 48.5 ₽", callback_data="buy_kyrgyzstan")
)

markup.add(
    types.InlineKeyboardButton("🇹🇯 Tajikistan : 30.5 ₽", callback_data="buy_tajikistan"),
    types.InlineKeyboardButton("🇺🇸 United States : 18 ₽", callback_data="buy_usa")
)

markup.add(
    types.InlineKeyboardButton("🇪🇬 Egypt : 21.5 ₽", callback_data="buy_egypt"),
    types.InlineKeyboardButton("🇮🇶 Iraq : 70.5 ₽", callback_data="buy_iraq")
)

markup.add(
    types.InlineKeyboardButton("🇹🇷 Turkey : 41.5 ₽", callback_data="buy_turkey"),
    types.InlineKeyboardButton("🇻🇪 Venezuela : 41.5 ₽", callback_data="buy_venezuela")
)

markup.add(
    types.InlineKeyboardButton("🇨🇴 Colombia : 17 ₽", callback_data="buy_colombia"),
    types.InlineKeyboardButton("🇿🇼 Zimbabwe : 18 ₽", callback_data="buy_zimbabwe")
)

markup.row(
    types.InlineKeyboardButton("[1]", callback_data="telegram"),
    types.InlineKeyboardButton("2", callback_data="telegram_page2"),
    types.InlineKeyboardButton("3", callback_data="telegram_page3"),
    types.InlineKeyboardButton("4", callback_data="telegram_page4"),
    types.InlineKeyboardButton("5", callback_data="telegram_page5"),
    types.InlineKeyboardButton("6", callback_data="telegram_page6"),
    types.InlineKeyboardButton("7", callback_data="telegram_page7"),
    types.InlineKeyboardButton("8", callback_data="telegram_page8"),
)

markup.add(
    types.InlineKeyboardButton("🔙 رجوع", callback_data="numbers")
)

bot.edit_message_text(
    "يمكنك شراء حسابات Telegram سليمة 100%\n\n"
    "✅ اختر الدولة التي تريد شراء رقم منها\n"
    "✅ السيرفر: (1)\n"
    "✅ الصفحة 1 من 8",
    chat_id=call.message.chat.id,
    message_id=call.message.message_id,
    reply_markup=markup
    )
    elif call.data == "telegram_page2":
elif call.data == "telegram_page2":

    markup = types.InlineKeyboardMarkup(row_width=2)

    markup.add(
        types.InlineKeyboardButton("🇫🇷 France : 52.5 ₽", callback_data="buy_france"),
        types.InlineKeyboardButton("🇦🇷 Argentina : 32.5 ₽", callback_data="buy_argentina")
    )

    markup.add(
        types.InlineKeyboardButton("🇳🇱 Netherlands : 48.5 ₽", callback_data="buy_netherlands"),
        types.InlineKeyboardButton("🇬🇧 United Kingdom : 27 ₽", callback_data="buy_uk")
    )

    markup.add(
        types.InlineKeyboardButton("🇭🇰 Hong Kong : 48.5 ₽", callback_data="buy_hongkong"),
        types.InlineKeyboardButton("🇹🇭 Thailand : 29 ₽", callback_data="buy_thailand")
    )

    markup.add(
        types.InlineKeyboardButton("🇼🇸 Samoa : 48.5 ₽", callback_data="buy_samoa"),
        types.InlineKeyboardButton("🇪🇸 Spain : 52.5 ₽", callback_data="buy_spain")
    )

    markup.add(
        types.InlineKeyboardButton("🇹🇳 Tunisia : 34.5 ₽", callback_data="buy_tunisia"),
        types.InlineKeyboardButton("🇸🇳 Senegal : 29 ₽", callback_data="buy_senegal")
    )

    markup.add(
        types.InlineKeyboardButton("🇲🇦 Morocco : 23.5 ₽", callback_data="buy_morocco"),
        types.InlineKeyboardButton("🇮🇳 India : 18 ₽", callback_data="buy_india")
    )

    markup.add(
        types.InlineKeyboardButton("🇱🇧 Lebanon : 56 ₽", callback_data="buy_lebanon"),
        types.InlineKeyboardButton("🇲🇿 Mozambique : 20 ₽", callback_data="buy_mozambique")
    )

    markup.add(
        types.InlineKeyboardButton("🇻🇳 Vietnam : 32.5 ₽", callback_data="buy_vietnam"),
        types.InlineKeyboardButton("🇬🇭 Ghana : 27 ₽", callback_data="buy_ghana")
    )

    markup.add(
        types.InlineKeyboardButton("🇮🇷 Iran : 20 ₽", callback_data="buy_iran"),
        types.InlineKeyboardButton("🇦🇪 United Arab Emirates : 70.5 ₽", callback_data="buy_uae")
    )

    markup.row(
        types.InlineKeyboardButton("1", callback_data="telegram"),
        types.InlineKeyboardButton("[2]", callback_data="telegram_page2"),
        types.InlineKeyboardButton("3", callback_data="telegram_page3"),
        types.InlineKeyboardButton("4", callback_data="telegram_page4"),
        types.InlineKeyboardButton("5", callback_data="telegram_page5"),
        types.InlineKeyboardButton("6", callback_data="telegram_page6"),
        types.InlineKeyboardButton("7", callback_data="telegram_page7"),
        types.InlineKeyboardButton("8", callback_data="telegram_page8"),
    )

    markup.add(
        types.InlineKeyboardButton("🔙 رجوع", callback_data="telegram")
    )

    bot.edit_message_text(
        "يمكنك شراء حسابات Telegram سليمة 100%\n\n"
        "✅ اختر الدولة التي تريد شراء رقم منها\n"
        "✅ السيرفر: (1)\n"
        "✅ الصفحة 2 من 8",
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=markup
)
elif call.data == "telegram_page3":

    markup = types.InlineKeyboardMarkup(row_width=2)

    markup.add(
        types.InlineKeyboardButton("🇬🇪 Georgia : 47.5 ₽", callback_data="buy_georgia"),
        types.InlineKeyboardButton("🇸🇱 Sierra Leone : 25.5 ₽", callback_data="buy_sierra")
    )

    markup.add(
        types.InlineKeyboardButton("🇵🇬 Papua New Guinea : 36.5 ₽", callback_data="buy_png"),
        types.InlineKeyboardButton("🇵🇰 Pakistan : 16.5 ₽", callback_data="buy_pakistan")
    )

    markup.add(
        types.InlineKeyboardButton("🇵🇪 Peru : 31 ₽", callback_data="buy_peru"),
        types.InlineKeyboardButton("🇦🇫 Afghanistan : 18.5 ₽", callback_data="buy_afghanistan")
    )

    markup.add(
        types.InlineKeyboardButton("🇬🇹 Guatemala : 36.5 ₽", callback_data="buy_guatemala"),
        types.InlineKeyboardButton("🇱🇰 Sri Lanka : 27.5 ₽", callback_data="buy_srilanka")
    )

    markup.add(
        types.InlineKeyboardButton("🇯🇴 Jordan : 47.5 ₽", callback_data="buy_jordan"),
        types.InlineKeyboardButton("🇸🇾 Syria : 31 ₽", callback_data="buy_syria")
    )

    markup.add(
        types.InlineKeyboardButton("🇵🇸 Palestine : 54.5 ₽", callback_data="buy_palestine"),
        types.InlineKeyboardButton("🇮🇩 Indonesia : 16.5 ₽", callback_data="buy_indonesia")
    )

    markup.add(
        types.InlineKeyboardButton("🇰🇭 Cambodia : 36.5 ₽", callback_data="buy_cambodia"),
        types.InlineKeyboardButton("🇸🇩 Sudan : 31 ₽", callback_data="buy_sudan")
    )

    markup.add(
        types.InlineKeyboardButton("🇸🇿 Eswatini : 22 ₽", callback_data="buy_eswatini"),
        types.InlineKeyboardButton("🇹🇱 Timor : 25.5 ₽", callback_data="buy_timor")
    )

    markup.add(
        types.InlineKeyboardButton("🇰🇷 South Korea : 91 ₽", callback_data="buy_korea"),
        types.InlineKeyboardButton("🇳🇬 Nigeria : 11 ₽", callback_data="buy_nigeria")
    )

    markup.row(
        types.InlineKeyboardButton("1", callback_data="telegram"),
        types.InlineKeyboardButton("2", callback_data="telegram_page2"),
        types.InlineKeyboardButton("[3]", callback_data="telegram_page3"),
        types.InlineKeyboardButton("4", callback_data="telegram_page4"),
        types.InlineKeyboardButton("5", callback_data="telegram_page5"),
        types.InlineKeyboardButton("6", callback_data="telegram_page6"),
        types.InlineKeyboardButton("7", callback_data="telegram_page7"),
        types.InlineKeyboardButton("8", callback_data="telegram_page8")
    )

    markup.add(
        types.InlineKeyboardButton("⬅️ رجوع", callback_data="numbers")
    )

    bot.edit_message_text(
        "100% سليمة Telegram يمكنك شراء حسابات\n\n"
        "✅ اختر الدولة التي تريد شراء رقم منها\n"
        "✅ السيرفر: (1)\n"
        "✅ الصفحة 3 من 8",
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=markup
)
elif call.data == "telegram_page4":
markup = types.InlineKeyboardMarkup(row_width=2)

markup.add(
    types.InlineKeyboardButton("🇮🇱 Israel : 41.5 ₽", callback_data="buy_israel"),
    types.InlineKeyboardButton("🇨🇳 China : 48.5 ₽", callback_data="buy_china")
)

markup.add(
    types.InlineKeyboardButton("🇵🇭 Philippines : 21.5 ₽", callback_data="buy_philippines"),
    types.InlineKeyboardButton("🇲🇼 Malawi : 41.5 ₽", callback_data="buy_malawi")
)

markup.add(
    types.InlineKeyboardButton("🇲🇾 Malaysia : 29 ₽", callback_data="buy_malaysia"),
    types.InlineKeyboardButton("🇮🇪 Ireland : 30.5 ₽", callback_data="buy_ireland")
)

markup.add(
    types.InlineKeyboardButton("🇦🇹 Austria : 32.5 ₽", callback_data="buy_austria"),
    types.InlineKeyboardButton("🇷🇸 Serbia : 36 ₽", callback_data="buy_serbia")
)

markup.add(
    types.InlineKeyboardButton("🇷🇴 Romania : 48.5 ₽", callback_data="buy_romania"),
    types.InlineKeyboardButton("🇸🇮 Slovenia : 56 ₽", callback_data="buy_slovenia")
)

markup.add(
    types.InlineKeyboardButton("🇳🇮 Nicaragua : 41.5 ₽", callback_data="buy_nicaragua"),
    types.InlineKeyboardButton("🇵🇾 Paraguay : 36 ₽", callback_data="buy_paraguay")
)

markup.add(
    types.InlineKeyboardButton("🇭🇺 Hungary : 38 ₽", callback_data="buy_hungary"),
    types.InlineKeyboardButton("🇳🇵 Nepal : 29 ₽", callback_data="buy_nepal")
)

markup.add(
    types.InlineKeyboardButton("🇺🇬 Uganda : 25 ₽", callback_data="buy_uganda"),
    types.InlineKeyboardButton("🇨🇦 Canada : 16 ₽", callback_data="buy_canada")
)

markup.add(
    types.InlineKeyboardButton("🇿🇲 Zambia : 25 ₽", callback_data="buy_zambia"),
    types.InlineKeyboardButton("🇸🇴 Somalia : 41.5 ₽", callback_data="buy_somalia")
)
elif call.data == "telegram_page5":
markup = types.InlineKeyboardMarkup(row_width=2)

markup.add(
    types.InlineKeyboardButton("🇵🇱 Poland : 23.5 ₽", callback_data="buy_poland"),
    types.InlineKeyboardButton("🇰🇪 Kenya : 21.5 ₽", callback_data="buy_kenya")
)

markup.add(
    types.InlineKeyboardButton("🇸🇻 El Salvador : 41.5 ₽", callback_data="buy_elsalvador"),
    types.InlineKeyboardButton("🇱🇾 Libya : 32.5 ₽", callback_data="buy_libya")
)

markup.add(
    types.InlineKeyboardButton("🇧🇴 Bolivia : 56 ₽", callback_data="buy_bolivia"),
    types.InlineKeyboardButton("🇫🇯 Fiji : 41.5 ₽", callback_data="buy_fiji")
)

markup.add(
    types.InlineKeyboardButton("🇹🇴 Tonga : 41.5 ₽", callback_data="buy_tonga"),
    types.InlineKeyboardButton("🇨🇷 Costa Rica : 32.5 ₽", callback_data="buy_costarica")
)

markup.add(
    types.InlineKeyboardButton("🇭🇳 Honduras : 41.5 ₽", callback_data="buy_honduras"),
    types.InlineKeyboardButton("🇯🇵 Japan : 52.5 ₽", callback_data="buy_japan")
)

markup.add(
    types.InlineKeyboardButton("🇳🇴 Norway : 114 ₽", callback_data="buy_norway"),
    types.InlineKeyboardButton("🇩🇰 Denmark : 114 ₽", callback_data="buy_denmark")
)

markup.add(
    types.InlineKeyboardButton("🇨🇱 Chile : 21.5 ₽", callback_data="buy_chile"),
    types.InlineKeyboardButton("🇨🇺 Cuba : 27 ₽", callback_data="buy_cuba")
)

markup.add(
    types.InlineKeyboardButton("🇵🇦 Panama : 41.5 ₽", callback_data="buy_panama"),
    types.InlineKeyboardButton("🇶🇦 Qatar : 92 ₽", callback_data="buy_qatar")
)

markup.add(
    types.InlineKeyboardButton("
elif call.data == "telegram_page6":
markup = types.InlineKeyboardMarkup(row_width=2)

markup.add(
    types.InlineKeyboardButton("🇦🇲 Armenia : 52.5 ₽", callback_data="buy_armenia"),
    types.InlineKeyboardButton("🇦🇴 Angola : 21.5 ₽", callback_data="buy_angola")
)

markup.add(
    types.InlineKeyboardButton("🇹🇩 Chad : 34.5 ₽", callback_data="buy_chad"),
    types.InlineKeyboardButton("🇩🇿 Algeria : 25 ₽", callback_data="buy_algeria")
)

markup.add(
    types.InlineKeyboardButton("🇸🇬 Singapore : 96 ₽", callback_data="buy_singapore"),
    types.InlineKeyboardButton("🇹🇲 Turkmenistan : 38 ₽", callback_data="buy_turkmenistan")
)

markup.add(
    types.InlineKeyboardButton("🇩🇪 Germany : 56 ₽", callback_data="buy_germany"),
    types.InlineKeyboardButton("🇧🇷 Brazil : 32.5 ₽", callback_data="buy_brazil")
)

markup.add(
    types.InlineKeyboardButton("🇲🇻 Maldives : 52.5 ₽", callback_data="buy_maldives"),
    types.InlineKeyboardButton("🇨🇿 Czech Republic : 41.5 ₽", callback_data="buy_czech")
)

markup.add(
    types.InlineKeyboardButton("🇧🇪 Belgium : 59.5 ₽", callback_data="buy_belgium"),
    types.InlineKeyboardButton("🇰🇮 Kiribati : 52.5 ₽", callback_data="buy_kiribati")
)

markup.add(
    types.InlineKeyboardButton("🇩🇯 Djibouti : 34.5 ₽", callback_data="buy_djibouti"),
    types.InlineKeyboardButton("🇦🇱
    elif call.data == "telegram_page7":

    markup = types.InlineKeyboardMarkup(row_width=2)

    markup.add(
        types.InlineKeyboardButton("🇭🇹 Haiti : 41.5 ₽", callback_data="buy_haiti"),
        types.InlineKeyboardButton("🇦🇿 Azerbaijan : 59.5 ₽", callback_data="buy_azerbaijan")
    )

    markup.add(
        types.InlineKeyboardButton("🇨🇻 Cape Verde : 41.5 ₽", callback_data="buy_capeverde"),
        types.InlineKeyboardButton("🇸🇨 Seychelles : 41.5 ₽", callback_data="buy_seychelles")
    )

    markup.add(
        types.InlineKeyboardButton("🇺🇾 Uruguay : 34.5 ₽", callback_data="buy_uruguay"),
        types.InlineKeyboardButton("🇬🇩 Grenada : 30.5 ₽", callback_data="buy_grenada")
    )

    markup.add(
        types.InlineKeyboardButton("🇨🇮 Ivory Coast : 34.5 ₽", callback_data="buy_ivorycoast"),
        types.InlineKeyboardButton("🇻🇨 Grenadines : 30.5 ₽", callback_data="buy_grenadines")
    )

    markup.add(
        types.InlineKeyboardButton("🇱🇨 Lucia : 41.5 ₽", callback_data="buy_lucia"),
        types.InlineKeyboardButton("🇸🇹 Principe : 52.5 ₽", callback_data="buy_principe")
    )

    markup.add(
        types.InlineKeyboardButton("🇲🇺 Mauritius : 41.5 ₽", callback_data="buy_mauritius"),
        types.InlineKeyboardButton("🇸🇷 Suriname : 41.5 ₽", callback_data="buy_suriname")
    )

    markup.add(
        types.InlineKeyboardButton("🇱🇸 Lesotho : 41.5 ₽", callback_data="buy_lesotho"),
        types.InlineKeyboardButton("🇧🇼 Botswana : 29 ₽", callback_data="buy_botswana")
    )

    markup.add(
        types.InlineKeyboardButton("🇩🇲 Dominica : 34.5 ₽", callback_data="buy_dominica"),
        types.InlineKeyboardButton("🇧🇿 Belize : 48.5 ₽", callback_data="buy_belize")
    )

    markup.add(
        types.InlineKeyboardButton("🇬🇦 Gabon : 36 ₽", callback_data="buy_gabon"),
        types.InlineKeyboardButton("🇨🇬 Congo : 30.5 ₽", callback_data="buy_congo")
)
elif call.data == "telegram_page8":
markup.add(
    types.InlineKeyboardButton("🇨🇫 Central Africa : 23.5 ₽", callback_data="buy_central_africa"),
    types.InlineKeyboardButton("🇱🇹 Lithuania : 70.5 ₽", callback_data="buy_lithuania")
)

markup.add(
    types.InlineKeyboardButton("🇬🇷 Greece : 48.5 ₽", callback_data="buy_greece"),
    types.InlineKeyboardButton("🇲🇷 Mauritania : 34.5 ₽", callback_data="buy_mauritania")
)

markup.add(
    types.InlineKeyboardButton("🇬🇺 Guam : 30.5 ₽", callback_data="buy_guam"),
    types.InlineKeyboardButton("🇸🇸 South Sudan : 38 ₽", callback_data="buy_south_sudan")
)

markup.add(
    types.InlineKeyboardButton("🇲🇬 Madagascar : 27 ₽", callback_data="buy_madagascar"),
    types.InlineKeyboardButton("🇧🇸 Bahamas : 41.5 ₽", callback_data="buy_bahamas")
)
