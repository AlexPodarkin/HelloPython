# Функции/методы в Python
# в Python можно миксовать типа возвращаемых данных Будь внимателен !
def nameFunction(arg):
    if arg == 1:
        return 'Целое'
    elif arg == 2.3:
        return 23
    else:
        return
argUser = 1
print(nameFunction(argUser))
print(type(nameFunction(argUser)))
argUser = 2.3
print(nameFunction(argUser))
print(type(nameFunction(argUser)))
argUser = 5
print(nameFunction(argUser))
print(type(nameFunction(argUser)))
a = None # так можно создать пустую переменную с неопределенным типом = <class 'NoneType'> 