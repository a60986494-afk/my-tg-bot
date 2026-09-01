import telebot

bot = telebot.TeleBot('8686974471:AAEq1858Drv_yNuC0d7BW17KaUmFaPZnoIU')

@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, 'Привет!')

bot.polling(none_stop=True)
