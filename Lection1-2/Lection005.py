# Управляющие конструкции if, if-else  # ОТСТУПЫ ВАЖНЫ
# поиск максимального числа
def SearchMax():             # def (функция/метод) в Python вызов SearchMax()
    a = int(input('a= '))
    b = int(input('b= '))
    if a > b:
        print(a)            # отступы ВАЖНЫ
    else:
        print(b)

userName = input('введите имя: ') # тут мы рассмотрели конструкцию elif
if userName == 'Маша':
    print('Ура Машка Ромашка !')
elif userName == 'Ильнар':
    print('Ильнар - Топ !')
elif userName == 'Alex':
    print('Я ждал тебя, Alex !')
else:
    print('Привет, ', userName)
