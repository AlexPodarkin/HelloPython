import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from button import kb_client

bot = Bot(tg_bot_token)
dp = Dispatcher(bot)
print('Go')
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_sticker(message.from_user.id,'CAACAgIAAxkBAAEG_p5jqCdl0LleIzqkLgvSYOKXDRgW-wACWyoAAiy9cUgb94vA1Xex2CwE')
    await message.reply('\U00002705 Пришли мне название  города на Английском\n'
    '\U00002328Ввод любого города можно осуществить с клавиатуры\n'
    '\U0001F447Или воспользоваться клавишами)', reply_markup=kb_client)


@dp.message_handler()
async def get_weather(message: types.Message):
    
    try:
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric'
        )
        data = r.json()
        #pprint(data)

        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        len_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        await message.reply(f"\U0001F4ACСегодня: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
            f'\U0001F3D9Погода в городе: {city}\n\U0001F321Температура: {cur_weather}°С\n'
        f'Влажносять: {humidity}%\nДавление: {pressure} мм.рт.ст\n\U0001F4A8Ветер: {wind}м*/с\n'
        f'Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\n'
        f'\U0001F4ABПродолжительность дня: {len_of_the_day}\nХорошего Дня Коллеги !')





    except:
        await message.reply('\U0001F9E0 Проверьте название города ! (на английском пожалуйста)\U0001F629')


if __name__ == '__main__':
    executor.start_polling(dp)