from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def deposit_menu():

    markup = InlineKeyboardMarkup(row_width=2)

    markup.add(
        InlineKeyboardButton("💙 FaucetPay", callback_data="pay_faucet")
    )

    markup.add(
        InlineKeyboardButton("🟢 CWallet", callback_data="pay_cwallet")
    )

    markup.add(
        InlineKeyboardButton("💎 TON", callback_data="pay_ton")
    )

    markup.add(
        InlineKeyboardButton("🟡 USDT BEP20", callback_data="pay_bep20")
    )

    markup.add(
        InlineKeyboardButton("🔵 USDT TRC20", callback_data="pay_trc20")
    )

    markup.add(
        InlineKeyboardButton("⚫ USDT ERC20", callback_data="pay_erc20")
    )

    markup.add(
        InlineKeyboardButton("🟣 USDT Polygon", callback_data="pay_polygon")
    )

    markup.add(
        InlineKeyboardButton("⬅️ رجوع", callback_data="home")
    )

    return markup
