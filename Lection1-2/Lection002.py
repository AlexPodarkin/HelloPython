#Типы данных и вывод!
print('введите a')
a = input()          # инпуты работают со строками!
print('введите b')
b = input()
print(f'первое число {a}, второе число {b}', 'сумма строк=', a + b)
#если хотим другой тип данных надо указать его
print('введите a')
a = int(input())  #то же самое с float()
print('введите b')
b = int(input())
print(f'первое число {a}, второе число {b}', 'сумма чисел = ', a + b)