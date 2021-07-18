import telebot
from setup import *
from parsing_data import *

bot = telebot.TeleBot(TOKEN)
output_titles = []
output_urls = Show_urls('')


@bot.message_handler(commands=['start'])  # може бути декілька параметрів
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)  # кнопки
    keyboard.row('/start', '/help', 'page-1', 'page-2',
                 'page-3', 'page-4', 'page-5')
    # відправляєм в чат ід хеллоу
    bot.send_message(
        message.chat.id, 'Choose a button', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])  # внутрішні кнопкі
def button(message):
    a = message.text[-1]
    output_titles = Show_titles(a)
    markup = telebot.types.InlineKeyboardMarkup()
    for i in range(len(output_titles)):
        markup.add(telebot.types.InlineKeyboardButton(
            text=output_titles[i], callback_data=i+1))
    bot.send_message(message.chat.id, f'page - {a}', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    answer = ''
    bot.answer_callback_query(
        callback_query_id=call.id, text='You check some button!')

    answer = show_new('https://stopgame.ru' +
                      output_urls[int(call.data)-1])

    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(
        call.message.chat.id, call.message.message_id)


bot.polling()
