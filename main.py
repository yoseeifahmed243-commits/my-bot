import telebot
from telebot import types

TOKEN = '8851361153:AAGhmCZJrEeAwC8JbA8l4ehyOUC6zBJe9hg'
bot = telebot.TeleBot(TOKEN)

SUPPORT = "https://t.me/elegramSMS_Support23"

# --- القائمة الرئيسية ---
def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("📱 شراء أرقام وهمية", callback_data="numbers"),
        types.InlineKeyboardButton("📢 خدمات الرشق والمتابعين", callback_data="rashq"),
        types.InlineKeyboardButton("💳 طرق الدفع والشحن", callback_data="payment"),
        types.InlineKeyboardButton("📞 التواصل مع الدعم", url=SUPPORT)
    )
    return markup

# --- زر الرجوع ---
def back_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("✖️ رجوع للقائمة الرئيسية", callback_data="main"))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 أهلاً بك في بوت السلطان\nاختيارك الأفضل للخدمات الرقمية.", reply_markup=main_menu())

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == "main":
        bot.edit_message_text("القائمة الرئيسية:", call.message.chat.id, call.message.message_id, reply_markup=main_menu())
    
    elif call.data == "numbers":
        text = "📱 قسم الأرقام الوهمية:\nنقدم أرقاماً مفعلة لتطبيقات:\n- تليجرام، واتساب، فيسبوك، جوجل، تيك توك، والمزيد.\n\nتواصل مع الدعم لطلب دولتك المطلوبة."
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=back_markup())
        
    elif call.data == "rashq":
        text = "📢 خدمات الرشق:\n- تليجرام (مشاهدات/أعضاء)\n- إنستجرام (فولو/لايكات)\n- تيك توك (مشاهدات/فولو)\n- يوتيوب (مشاهدات/ساعات)\n\nأسعار خاصة للموزعين!"
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=back_markup())
        
    elif call.data == "payment":
        text = "💳 طرق الدفع المتاحة:\n\n• Cwallet ID: 61824874\n• FaucetPay: TelegramSMS\n• USDT (TRC-20, BEP-20, Polygon)\n• عملات TON\n\nيرجى إرسال الإيصال للدعم بعد التحويل."
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=back_markup())

if __name__ == "__main__":
    bot.remove_webhook()
    bot.polling(none_stop=True)
