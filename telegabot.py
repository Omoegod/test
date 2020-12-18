import telebot

bot = telebot.TeleBot('1409141931:AAEIioEkKLK3pjrjRacBPjS5Z0Z6b04XZK0')

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling(none_stop=True)