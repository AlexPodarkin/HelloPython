from math import pi
import random


def Task1():
    d = 0.001        # заданная точность
    print('заданная точность = ', d)
    count = 0
    while d % 1 != 0:  # считаем количество цифр после запятой
        d *= 10
        count += 1
    res = (pi * 10**count) // 1 / 10**count  # без использования round
    print('число пи с заданной точностью = ', res)
    # print(f'число пи с заданной точностью = {round(pi, count)}') # используя round


def Task2():
    divider = 2
    n = 15
    print('Cписок простых множителей числа', n)
    res_list = []
    while n > 1:  # находим множители с помощью проверки и деления числа.
        while n % divider == 0:
            res_list.append(divider)
            n = n / divider
        divider += 1
    print('=>', res_list)


def Task3():
    init_list = [1, 2, 3, 2, 4, 4]
    print('исходный список => ', init_list)
    result_list = []
    for i in init_list:
        if i not in result_list:
            result_list.append(i)
    print('неповторяющиеся элементы:', result_list)


def Task4():
    k = 3
    random_list = []
    # формируем случайным образом список коэффициентов (значения от 0 до 100)
    for i in range(k + 1):
        random_list.append(random.randint(0, 100))
    result = ""
    if len(random_list) < 1:  # если длина меньше 1 то x = 0
        result = "x = 0"
    else:                   # формируем многочлен
        for i in range(len(random_list)):
            if i != len(random_list) - 1 and random_list[i] != 0 and i != len(random_list) - 2:
                result += f"{random_list[i]}x^{len(random_list) - i - 1}"
                if random_list[i + 1] != 0:
                    result += " + "
            elif i == len(random_list) - 2 and random_list[i] != 0:
                result += f"{random_list[i]}x"
                if random_list[i + 1] != 0:
                    result += " + "
            elif i == len(random_list) - 1 and random_list[i] != 0:
                result += f"{random_list[i]} = 0"
            elif i == len(random_list) - 1 and random_list[i] == 0:
                result += " = 0"
    print('многочлен степени k:', result)
    with open("file.txt", 'w') as data:  # записываем результат в файл
        data.write(result)


Task1()
print('===============X=================')
Task2()
print('===============X=================')
Task3()
print('===============X=================')
Task4()
