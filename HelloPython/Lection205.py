# словари

dictionary = {}                                 # создать пустой словарь
dictionary = {'up': 'vverh', 'down': 'vniz'}    # создать словарь со значениями
print(dictionary)           # печать весь словарь
print(dictionary['up'])     # печать по ключу

for k in dictionary.keys():   # печать ключей
    print(k)

for k in dictionary.values(): # печать значений
    print(k)
print('==============================')
for k in dictionary:         # печать значений
    print(dictionary[k])     # если мы хотик ключи, код print(dictionary) просто без индекса

del dictionary['down'] # удалени элемента по ключу
print(dictionary)

for i in dictionary:
    print(i, dictionary[i]) # печать ключ-значение

dictionary['up'] = 'izmenil' # изменение значения в словаре
print(dictionary['up'])



