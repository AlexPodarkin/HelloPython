# особенности работы с листами

list1 = [1, 2, 3, 4, 5]
list2 = list1

print(list2)
print(list1)

# мы поменяли значение в листе 1 (по отогу эта запись поменяет значение во втором листе)
list1[0] = 50
list2[4] = 70  # обратное тоже верно

print(list1)
print(list2)
print('==================')
print(list1.pop())  # удаление последнего элемента
print(list1)
print(list1.pop(0))  # удаление конкретного элемента
print(list1)
# добавление элементы на позицию(вставить на первый индекс цифру 5), произойдет сдвиг вправо
print(list1.insert(1, 5))
print(list1)
