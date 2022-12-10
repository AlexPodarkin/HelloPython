# List Comprehension
# Нужен для быстрого создания списков

list1 = []          # так мы раньше создавали список с четными значениями
for i in range(21):
    if i % 2 == 0:
       list1.append(i)

list2 = [i for i in range(0, 21)] # так можно коротко создать список из 20 элементов 
print(list2)

print('добавили условие if и создали список четных элементов')
list3 = [i for i in range(0, 21) if i%2 == 0] 
print(list3)

print('список кортежей')
list4 = [(i, i) for i in range(0, 21) if i%2 == 0]  
print(list4)

# создали элементарную функцию
def func(x):
    return x**2
print('возвели четные эл. списка в квадрат, исползуя функцию и короткую запись')
list5 = [func(i) for i in range(2, 21) if i%2 == 0] 
print(list5)
print('для наглядности можно вывести кортежами элемент и его квадрат')
list5 = [(i, func(i)) for i in range(2, 21) if i%2 == 0]
print(list5)
# механизм List Comprehension упрощает запись.

print('задачка')
list1 = [1, 2, 3, 5, 8, 15, 23, 38]
result = list((i, i*i) for i in list1 if i % 2 == 0)
print(result)