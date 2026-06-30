import asyncio
import aiosqlite
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

# --- إعدادات الإدارة ---
BOT_TOKEN = "8788796273:AAEypT5ZhFLNFyEGeccUfPtSIzNFcGnYjzA"
ADMIN_ID = 8767607098  # الـ ID الخاص بك
ADMIN_CHANNEL_ID = -4421674702  # ID القناة
CWALLET_ID = "61824874" # معرف Cwallet الخاص بك

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# --- بيانات المحافظ ---
ADDRESSES = {
    "trc20": "TRHUB8kuMpdCoDzST6c4AJ4cJdk6tToz97",
    "bep20": "0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155",
    "erc20": "0x8D7dDE7719e9d6D3e5175CE170Fae00372715493",
    "poly": "0xA7fE0a5Ae6Adcd5b47df238F836449b4d0866155",
    "sol": "4DQ8NZuS3Z5mRKoFSKGwKnUbZbCvvBwauCkpKRfRVtYy",
    "ton": "UQBEejOPxeZK8DyVwkAVQznE1FrMi0EbxxJSia7MhS4H1Co7"
}

class DepositStates(StatesGroup):
    waiting_for_tx = State()

# --- قاعدة البيانات ---
async def init_db():
    async with aiosqlite.connect("database.db") as db:
        await db.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, balance REAL DEFAULT 0)')
        await db.commit()

# --- الأوامر الأساسية ---
@dp.message(Command("start"))
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="💰 رصيدي", callback_data="profile")],
        [types.InlineKeyboardButton(text="💳 شحن الرصيد", callback_data="deposit")],
        [types.InlineKeyboardButton(text="🛒 شراء رقم", callback_data="buy_number")],
        [types.InlineKeyboardButton(text="🎧 الدعم الفني", url="https://t.me/SULTANPRO_SUPPORT")]
    ])
    await message.answer("مرحباً بك في بوت الأرقام!\nاختر الخدمة التي تحتاجها:", reply_markup=markup)

# --- أمر الإدارة (إضافة رصيد) ---
@dp.message(Command("add"))
async def add_balance(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        args = message.text.split()
        if len(args) == 3:
            user_id, amount = int(args[1]), float(args[2])
            async with aiosqlite.connect("database.db") as db:
                await db.execute('UPDATE users SET balance = balance + ? WHERE user_id = ?', (amount, user_id))
                await db.commit()
            await message.answer(f"✅ تمت إضافة {amount} روبل للمستخدم {user_id}")

# --- نظام الإيداع ---
@dp.callback_query(F.data == "deposit")
async def deposit_menu(callback: types.CallbackQuery):
    markup = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="USDT - TRC20", callback_data="dep_trc20")],
        [types.InlineKeyboardButton(text="USDT - BEP20", callback_data="dep_bep20")],
        [types.InlineKeyboardButton(text="USDT - ERC20", callback_data="dep_erc20")],
        [types.InlineKeyboardButton(text="USDT - POLYGON", callback_data="dep_poly")],
        [types.InlineKeyboardButton(text="USDT - SOLANA", callback_data="dep_sol")],
        [types.InlineKeyboardButton(text="TON", callback_data="dep_ton")]
    ])
    await callback.message.answer("يرجى اختيار العملة والشبكة للإيداع:", reply_markup=markup)

@dp.callback_query(F.data.startswith("dep_"))
async def show_address(callback: types.CallbackQuery, state: FSMContext):
    net = callback.data.split("_")[1]
    await callback.message.answer(
        f"أرسل العملة لشبكة <b>{net.upper()}</b> إلى:\n<code>{ADDRESSES.get(net)}</code>\n\n"
        f"Cwallet ID الخاص بنا: <code>{CWALLET_ID}</code>\n\n"
        "أرسل رقم العملية (TX ID) هنا ليقوم الدعم بالتأكيد."
    )
    await state.set_state(DepositStates.waiting_for_tx)

@dp.message(DepositStates.waiting_for_tx)
async def handle_deposit(message: types.Message, state: FSMContext):
    await bot.send_message(ADMIN_CHANNEL_ID, f"🔔 طلب شحن جديد!\nالمستخدم: @{message.from_user.username}\nID: {message.from_user.id}\nالعملية: {message.text}")
    await message.answer("تم إرسال طلبك للإدارة، سيتم شحن رصيدك فور التأكيد.")
    await state.clear()

# --- التشغيل ---
async def main():
    await init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
