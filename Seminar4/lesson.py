""" data = open('file.txt', 'a', encoding='UTF-8')

while True:
    string = input('Введите строку: ')
    if string == '':
        break
    data.write(string + '\n')

data.close()
data = open('file.txt', 'r', encoding='UTF-8')

for s in data.readlines():
    print(s, end='')
    print(f'Количество символов = {len(s)}')
    print(f"Количество слов = {len(s.split())}")
    print()
data.close()
 """

""" Больше предыдущего
На вход программе подается строка текста из натуральных чисел.
Из неё формируется список чисел.
Напишите программу подсчета количества чисел,
которые больше предшествующего им в этом списке числа,
то есть, стоят вслед за меньшим числом.
Формат входных данных
 """

a = input('Введите строку: ')
list = a.split(' ')
for i in range(len(list)):
    list[i] = int(list[i])
count = 0
num = list[0]
for i in list:
    if i > num:
        count += 1
    num = i
print(count)


""" На вход программе подается строка
текста из разделенных пробелами натуральных чисел.
Формат выходных данных
Программа должна вывести одно число – количество элементов списка, больших предыдущего.
Тестовые данные
Sample Input 1:
1 2 3 4 5
Sample Output 1:
4
Sample Input 2:
1 1 3 2 2 1 1 1 1
Sample Output 2:
1
Sample Input 3:
5 4 3 2 1
Sample Output 3:
0
 """

""" На вход программе подается строка текста из натуральных чисел. 
Из элементов строки формируется список чисел. Напишите программу, 
которая меняет местами соседние элементы списка(a[0] c a[1], a[2] c a[3] и т.д.).
 Если в списке нечетное количество элементов, то последний остается на своем месте.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.
#
# Формат выходных данных
# Программа должна вывести измененный список, разделяя его элементы одним пробелом.
#
# Тестовые данные """

