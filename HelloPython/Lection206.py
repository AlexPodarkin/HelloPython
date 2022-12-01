# Множества

colors = {'red', 'green', 'blue', }  # создаем множества
print(type(colors))                 # узнаем тип
print(colors)                       # печатаем множество
# если мы добавис то что уже есть изменений не будет
colors.add('gray')
colors.remove('green')              # удаление
# удаление (если элемента уже нет ошибки не будет в оличии от remove)
colors.discard('green')
print(colors)
colors.clear()                      # отчистить множества
print(colors)                       # пустое set{} иножество

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()            # копия множества
u = a.union(b)          # объеденение множеств
i = a.intersection(b)   # пересечение
dl = a. difference(b)   # разница
dr = b.difference(a)    #
q = a \
    .union(b) \
        .difference(a.intersection(b))
print(q)
f = frozenset(a) # создать замороженное множество от "а" множества
