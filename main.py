import telebot
import time

TOKEN = '8851361153:AAGhmCZJrEeAwC8JbA8l4ehyOUC6zBJe9hg'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "✅ البوت شغال يا بطل!")

if __name__ == "__main__":
    print("جاري تشغيل البوت...")
    bot.remove_webhook()
    time.sleep(1)
    bot.polling(none_stop=True)
