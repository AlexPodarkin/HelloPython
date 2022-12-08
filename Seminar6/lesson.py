""" 1.Вводится список целых чисел в одну строчку через пробел.
  Необходимо оставить в нем только двузначные числа.
   Реализовать программу с использованием функции filter.
      Результат отобразить на экране в виде последовательности
       оставшихся чисел в одну строчку через пробел.
    пример  - 8 11 0 - 23 140 1 = > 11 - 23

 """

string_num = '3123 21 32132 -21 -132 1213 1 12'.split()
print(string_num)
string_num = filter(lambda i: len(str(abs(int(i)))) == 2, string_num)
print(*string_num)

# filter
a = ( "a", 'b', '2', '3' ,'c')
b = ( 'a' , 'b' , 'c')
c = ( '1', '2', '3')
 

b= filter(str.isalpha, a)
c= filter(str.isdigit, a)

print(*b)
print(*c)

# ZIP
users = ['user1','user2','user3','user4','user5']
ids = [4, 5, 9, 14, 7]
salary = [111,222,333]

a,b,c = map(list,zip(users, ids, salary))
print(a,b,c, sep="\n")
a,b,c= map(list,zip(a,b,c))

print(a,b,c, sep="\n")

