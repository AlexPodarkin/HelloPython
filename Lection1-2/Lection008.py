# немного о списках ( работа со списками )
numbers = [1, 2, 3, 4, 5]  # создание списка
print(numbers)

numbers = list(range(1, 6))  # с помощю range (внимание range != list)
print(numbers)

numbers[0] = 10
print(numbers)

for i in numbers:
    i *= 2
    print(i)
print(numbers)

ran = range(1, 6)
print(type(ran))                        # тут будет <class 'range'>
numbers = list(ran)                     # привдение типом ( внимание range != list )
print(type(numbers))                    # тут будет <class 'list'>
print(len(numbers))                     # кол-во элементов в списке
numbers.append(25)                      # добавить элемент в конец списка
print(25 in numbers)                    # True есть ли 25 в списке
print(numbers == [1, 2, 3, 4, 5, 25])   # True проверка списка 
print(numbers)
numbers.remove(25)                      # Удалить элемент из списка [1, 2, 3, 4, 5]
numbers.remove(numbers[0])              # Удалить конкретный элемент из списка [2, 3, 4, 5]  
del numbers[0]                          # Удалить конкретный элемент из списка другой вариант [3, 4, 5]
print(numbers)
