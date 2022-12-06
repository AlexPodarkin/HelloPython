def name_f(x):    # обычная функция
    return x + 5


print(type(name_f))  # <class 'function'>

lol = name_f  # функция может быть положена в переменную

print(name_f(2))  # 7
print(lol(2))    # 7


def Vnimanie(func, value):  # метод, который принимает в аргумент функцию и значение
    print(func(value))


Vnimanie(name_f, 5)  # 10
Vnimanie(lol, 5)    # 10
print('===================x======================')
# теперь попробуем функцию с 2мя переменными


def sum(x, y):
    return x + y


def mult(x, y):
    return x * y


def metod(name, a, b):  # метод, который принимает в аргумент функцию и ДВА значения
    print(name(a, b))
    # return name(a, b)


metod(mult, 5, 5)
print('запись в помощю лямбды')
# не обязательно класть в переменную(можно использовать в контексте)
name_p = lambda x, y: y*x # name_p = lambda x: x*x аналогично=> def name_p(x, y): return y*x
print(name_p(5, 5))

metod(name_p, 3, 3)
# Лямбда-функция в Python