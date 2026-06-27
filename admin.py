from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import ADMIN_ID

def is_admin(user_id):
    return user_id == ADMIN_ID

def admin_menu():
    markup = InlineKeyboardMarkup(row_width=2)

    markup.add(
        InlineKeyboardButton("💰 إضافة رصيد", callback_data="admin_add_balance"),
        InlineKeyboardButton("➖ خصم رصيد", callback_data="admin_remove_balance")
    )

    markup.add(
        InlineKeyboardButton("📋 الطلبات", callback_data="admin_orders"),
        InlineKeyboardButton("💳 طلبات الشحن", callback_data="admin_deposits")
    )

    markup.add(
        InlineKeyboardButton("📢 إذاعة", callback_data="admin_broadcast"),
        InlineKeyboardButton("📊 الإحصائيات", callback_data="admin_stats")
    )

    return markup
