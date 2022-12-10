def nameFunction (*params):
    res: str = ""           # переменная двоеточие тип данных, если хотим int пишем res: int = 0 / или просто res = 0 
    for item in params:
        res += item         # здесь мы ожидаем получение строки !
    return res

print(nameFunction('a', 'a', 'a', ))
print(nameFunction('a', '1', '2', ))
# print(nameFunction(1, 2 )) # TypeError: ...