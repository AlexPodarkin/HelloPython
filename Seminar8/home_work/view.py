

def menu():
    print('\n' + '-' * 22)
    print('\tМеню:')
    print('-' * 22)
    print('1. Добавить сотрудника')
    print('2. Найти сотрудника')
    print('3. Удалить сотрудника')
    print('4. Экспортировать данные в формате json')
    print('5. Закончить работу')

    choice = int(input('Выберите пункт меню: '))
    while choice < 1 or choice > 5:
        print('неверный ввод !!! ')
        choice = int(input('Введите номер необходимого действия: '))
    else:
        return choice