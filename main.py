import telebot

bot = telebot.TeleBot('6597281045:AAEEN4NdSBF8GrEWtOT3lS5g7mxRFe1YbEQ')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Как тебя зовут?')


@bot.message_handler(commands=['product'])
def main(message):
    bot.send_message(message.chat.id, 'Сердце из половинок /nJensen Ross Ackles /nЁлочная игрушка - Олень')


@bot.message_handler(commands=['price'])
def main(message):
    bot.send_message(message.chat.id, '500 рублей /n500 рублей /n300 рублей')


@bot.message_handler(commands=['link'])
def main(message):
    bot.send_message(message.chat.id, 'Нажми, чтоб попасть в [мир брелочков](https://vk.com/kmshop_katiko)',
                     parse_mode='Markdown')


bot.infinity_polling()