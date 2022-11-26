
import random


def task1():
    num = float(input("Введите число : "))  # Преобразуем строку в дробное
    a = int(num)
    b = num - int(num)
    print("целая часть =", a)
    print("дробная =", b)
    sum = 0
# "len(str(b)) - 2" = это нужно для приведения остатка к целому "-2" что бы убрать из расчета "0,""  и оставить то что после запятой
    b = b * (10 ** (len(str(b)) - 2))
    while (a != 0):  # нахождение суммы целой части числа
        sum = sum + a % 10
        a = a // 10
    while (b != 0):  # нахождение суммы дробной части числа
        sum = sum + b % 10  # 
        b = b // 10
    print("Сумма цифр равно:", int(sum))


def task2():
    valueN = int(input('Введите N: '))
    resultList = []

    def multiplication(k):
        if (k > 0):
            # ещевариант можно сделать без списка добавив=> print(result, sep=",",end=" ")
            result = k*multiplication(k-1)
        else:
            result = 1
        resultList.append(result)
        return result
    multiplication(valueN)
    del resultList[0]
    print(resultList)


# я так понимаю в задаче словарь, т.к мы еще не знакомы со словарем
# с вашего позволения я сделаю последовательность через список
def task3():
    print('task 3 =>')
    valueN = 6
    resultList = []

    def recurr(k):
        if (k > 0):
            # ещевариант можно сделать без списка добавив=> print(result, sep=",",end=" ")
            # решение аналогично 2 задаче, изменена формула.
            result = recurr(k-1) + 3
        else:
            result = 1
        resultList.append(result)
        return result
    recurr(valueN)
    del resultList[0]
    print(resultList)

def task4():
    n = int(input('Введите размер списка: '))
    spisok = [0] * n
    for i in range(len(spisok)):
        spisok[i] = input(f' введите {i+1} элемент: ')

    print('исходный список =>', spisok)  # как я понял этот способ не Тру))))
    random.shuffle(spisok)
    print('перемешанный список =>', spisok)
# задачу с файлами не решал. вы сказали она не обязатеньна к выполнению
# т.к мы еще не работали с файлами.

task1()
task2()
task3()
task4()

