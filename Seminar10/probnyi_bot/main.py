import telebot
from telebot import types

bot = telebot.TeleBot('5629640823:AAGNiW-uQuWHzZibfwWL0IQ26uEYoitJ8VI')


@bot.message_handler(commands=['start'])  # команда старт
def start(message):
    name = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>' + '\nпросто напиши слово "Кнопки" без кавычек )  '
    bot.send_message(message.chat.id, name, parse_mode='html')


# ниже можно указать аргумент " content_types=['text'] " это текст который вводит пользователь
@bot.message_handler()
def get_user_text(message):
    if message.text == 'привет':  # можем отслеживать сообщения пользователя
        bot.send_message(message.chat.id, 'И тебе привет!', parse_mode='html')
    elif message.text == 'ид':
        bot.send_message(
            message.chat.id, f'Твой ID: {message.from_user.id}', parse_mode='html')
    elif message.text == 'фото':
        photo = open('photo.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close
    elif message.text == 'вк':
        def website(message):
            knopka = types.InlineKeyboardMarkup()
            knopka.add(types.InlineKeyboardButton(
                'Посетить ВК', url='https://vk.com/andr.podarkin'))
            bot.send_message(message.chat.id, 'Следуй', reply_markup=knopka)
        website(message)
    elif message.text == 'Кнопки':
        def website(message):
            knopka = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1) 
            # аргументы расположение кнопок row_width=1 можно без аргументов
            website = types.KeyboardButton('привет')
            start = types.KeyboardButton('ид')
            foto = types.KeyboardButton('фото')
            vk = types.KeyboardButton('вк')
            knopka.add(website, start, foto, vk)
            bot.send_message(message.chat.id, 'Выбирай!', reply_markup=knopka)
        website(message)
    else:
        bot.send_message(message.chat.id, 'Чувак) Просто на чиле введи слово "Кнопки"',
                         parse_mode='html')
    

print('Go')
bot.polling(non_stop=True)
