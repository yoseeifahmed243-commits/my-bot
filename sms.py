from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from services import SERVICES, calc_price

def sms_menu():
    markup = InlineKeyboardMarkup(row_width=1)

    for key, service in SERVICES.items():
        price = calc_price(service["rub_price"])

        markup.add(
            InlineKeyboardButton(
                f'{service["name"]} | ${price}',
                callback_data=f"sms_{key}"
            )
        )

    markup.add(
        InlineKeyboardButton("⬅️ رجوع", callback_data="home")
    )

    return markup
