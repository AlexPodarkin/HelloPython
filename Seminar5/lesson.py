""" Объявите анонимную (лямбда) функцию для определения вхождения 
в переданную ей строку фрагмента "plr". То есть, функция должна возвращать True,
если такой фрагмент присутствует в строке и False - в противном случае. """

input_str = 'jdskfh plr kjkh'
result = (lambda x: 'plr' in x)  # аналогично result = (lambda x: 'plr' in x)(input_str)
print(result(input_str))


""" задача по на хождению НОД """
a = 60
b = 15
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print('НОД = ', a)

""" задача по на хождению НОД , быстрый способ"""

import random
a = random.randint(33, 99)
b = random.randint(33, 99)
c = [a, b]
print(c)
while max(a, b) % min(a, b) != 0:
    if a > b:
        a = a % b
    elif a < b:
        b = b % a
print(min(a, b))

print((lambda x: 'PLR' in x)('daPLRsd'))  # во вторых скобках можно использовать сраз input()

