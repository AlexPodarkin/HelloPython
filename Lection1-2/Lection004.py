# логические операции
a = 15 > 4 and 5 > 3  # также работает проверка не равенства != и равенства ==
print(a)
a = [1, 2]
b = [1, 2]
print(a == b)  # также работают списки сравнение поэлементно
a = 1 < 3 < 5
print(a)  # тройные сравнения и четверне тоже работают :)

# or  оператор = или (ТТТК одно высказывание истина)
f = 1 > 2 or 4 < 6 or 5 < 1
print(f)
list = [1, 2, 3, 4]
print(2 in list)  # есть ли 2 в списке
print(not 2 in list) #отрицание
proverka_el_list = list[0] % 2 == 0 #проверка элемента листа на четность
print(proverka_el_list)
