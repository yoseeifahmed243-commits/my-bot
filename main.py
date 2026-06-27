import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import (
    TOKEN,
    BOT_NAME,
    SUPPORT,
    ADMIN_ID,
    TON_ADDRESS,
    TRC20_ADDRESS,
    ERC20_ADDRESS,
    BEP20_ADDRESS,
    POLYGON_ADDRESS,
    FAUCETPAY,
    CWALLET
)
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
        InlineKeyboardButton("📈 خدمات الرشق", callback_data="smm")
    )

    markup.add(
        InlineKeyboardButton("🎁 الإحالة", callback_data="referral"),
        InlineKeyboardButton(
            "📞 الدعم",
            url=f"https://t.me/{SUPPORT.replace('@','')}"
        )
    )

    return markup


@bot.message_handler(commands=["start"])
def start(message):

    database.add_user(message.from_user.id)

    balance = database.get_balance(message.from_user.id)

    bot.send_message(
        message.chat.id,
        f"""
✨ أهلاً بك في {BOT_NAME}

💰 رصيدك: {balance}$

اختر الخدمة من الأسفل.
""",
        reply_markup=main_menu()
    )


@bot.message_handler(commands=["admin"])
def admin(message):

    if not is_admin(message.from_user.id):
        return

    bot.send_message(
        message.chat.id,
        "👑 لوحة الأدمن",
        reply_markup=admin_menu()
    )


@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):

    # القائمة الرئيسية
    if call.data == "home":

        bot.edit_message_text(
            "🏠 القائمة الرئيسية",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=main_menu()
        )

    # شراء SMS
    elif call.data == "sms":

        bot.edit_message_text(
            "📱 اختر الخدمة",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=sms_menu()
        )

    # اختيار Telegram أو WhatsApp
    elif call.data.startswith("sms_"):

        service = call.data.replace("sms_", "")

        bot.edit_message_text(
            "🌍 اختر الدولة",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=countries_menu(service)
        )

    # شحن الرصيد
    elif call.data == "deposit":

        bot.edit_message_text(
            "💳 اختر طريقة الشحن",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=deposit_menu()
    )
            # شراء رقم
    elif call.data.startswith("buy_"):

        _, service, country = call.data.split("_", 2)

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
            "zimbabwe": 13,
            "philippines": 10,
            "vietnam": 10,
            "indonesia": 10,
            "thailand": 10,
            "canada": 10,
            "southafrica": 10,
            "morocco": 13,
            "libya": 10,
            "france": 10,
            "uk": 10
        }

        base_price = prices.get(country, 10)
        final_price = round(base_price * 1.30, 2)

        markup = InlineKeyboardMarkup()

        markup.add(
            InlineKeyboardButton(
                f"🛒 شراء مقابل {final_price} ₽",
                callback_data=f"confirm_{service}_{country}"
            )
        )

        markup.add(
            InlineKeyboardButton(
                "⬅️ رجوع",
                callback_data=f"sms_{service}"
            )
        )

        bot.edit_message_text(
            f"""📲 الخدمة: {service.title()}

🌍 الدولة: {country}

💰 السعر: {final_price} ₽

اضغط شراء لإرسال الطلب.""",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )

    # تأكيد الشراء
    elif call.data.startswith("confirm_"):

        _, service, country = call.data.split("_", 2)

        user = call.from_user

        bot.send_message(
            ADMIN_ID,
            f"""📥 طلب جديد

👤 الاسم: {user.first_name}

🆔 ID: {user.id}

📲 الخدمة: {service}

🌍 الدولة: {country}
"""
        )

        bot.edit_message_text(
            """✅ تم استلام طلبك.

📩 سيتم التواصل معك خلال دقائق.""",
            call.message.chat.id,
            call.message.message_id
        )

    # حسابي
    elif call.data == "account":

        balance = database.get_balance(call.from_user.id)

        bot.send_message(
            call.message.chat.id,
            f"""👤 حسابك

🆔 ID : {call.from_user.id}

💰 الرصيد : {balance}$"""
        )

    # الرشق
    elif call.data == "smm":

        bot.answer_callback_query(
            call.id,
            "قريباً..."
        )

    # الإحالة
    elif call.data == "referral":

        bot.answer_callback_query(
            call.id,
            "قريباً..."
                                             )    # طرق الدفع
    elif call.data.startswith("pay_"):

        method = call.data.replace("pay_", "")

        bot.send_message(
            call.message.chat.id,
            # طرق الدفع
elif call.data.startswith("pay_"):

    method = call.data.replace("pay_", "")

    addresses = {
        # طرق الدفع
elif call.data.startswith("pay_"):

    method = call.data.replace("pay_", "")

    addresses = {
        "ton": TON_ADDRESS,
        "trc20": TRC20_ADDRESS,
        "erc20": ERC20_ADDRESS,
        "bep20": BEP20_ADDRESS,
        "polygon": POLYGON_ADDRESS,
        "faucetpay": FAUCETPAY,
        "cwallet": CWALLET
    }

    address = addresses.get(method, "غير متوفر")

    bot.send_message(
        call.message.chat.id,
        f"""💳 طريقة الدفع: {method.upper()}

📍 عنوان الدفع:

{address}

📸 بعد التحويل أرسل صورة التحويل مع كتابة المبلغ.

مثال:
20 USDT"""
    )    # طلبات الأدمن
    elif call.data == "admin_orders":

        bot.send_message(
            call.message.chat.id,
            "📦 سيتم عرض طلبات الشراء هنا."
        )

    elif call.data == "admin_deposits":

        bot.send_message(
            call.message.chat.id,
            "💳 سيتم عرض طلبات الشحن هنا."
        )

    elif call.data == "admin_users":

        bot.send_message(
            call.message.chat.id,
            f"👥 عدد المستخدمين: {database.total_users()}"
        )

    elif call.data == "admin_stats":

        bot.send_message(
            call.message.chat.id,
            f"""📊 الإحصائيات

👥 المستخدمون: {database.total_users()}

📦 الطلبات: {database.total_orders()}
"""
        )


# استقبال الصور
@bot.message_handler(content_types=["photo"])
def receive_photo(message):

    caption = message.caption if message.caption else "بدون مبلغ"

    bot.forward_message(
        ADMIN_ID,
        message.chat.id,
        message.message_id
    )

    bot.send_message(
        ADMIN_ID,
        f"""💳 طلب شحن جديد

👤 {message.from_user.first_name}

🆔 {message.from_user.id}

💰 {caption}
"""
    )

    bot.edit_message_text(
    f"""✅ تم استلام طلبك.

📩 سيتم التواصل معك خلال دقائق.

📞 الدعم:
{SUPPORT}""",
    call.message.chat.id,
    call.message.message_id
    )
