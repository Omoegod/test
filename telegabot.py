import telebot

bot = telebot.OmoegodBot('1409141931:AAEIioEkKLK3pjrjRacBPjS5Z0Z6b04XZK0')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

 bot.polling()   