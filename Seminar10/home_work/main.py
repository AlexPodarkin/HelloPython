from config import open_weather_token
import requests
import datetime
from pprint import pprint

def get_waether(city, open_weather_token):
    try:
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric'
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
        print(f"\nСегодня: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
            f'Погода в городе: {city}\nТемпература: {cur_weather}°С\n'
        f'Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind}м*/с\n'
        f'Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\n'
        f'Продолжительность дня: {len_of_the_day}\nХорошего Дня Друг !')





    except Exception as ex:
        print(ex)
        print('Проверьте название города ! (на английском пожалуйста)')


def main():
    city = input('Введите город: ')
    get_waether(city, open_weather_token)

if __name__== '__main__':
    main()

