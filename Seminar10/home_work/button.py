from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

but1 = KeyboardButton('Astrakhan')
but2 = KeyboardButton('Moscow')
but3 = KeyboardButton('Krasnodar')

kb_client = ReplyKeyboardMarkup()

kb_client.add(but1).add(but2).add(but3)