# ФАЙЛЫ

# colors = ['res', 'green', 'blue']
# data = open('file.txt', 'a')    # в скобках указывается путь к файлу и мод с которым будем работать через запятую
# data.writelines(colors) # разделителей не будет
# data.write('\nLINE2\n') 
# data.write('LINE3 \n') 
# data.close  # закрывается подключение, прерывается работа с файлом

# -----------------------------------------

# with open('file.txt', 'w') as data:
#     data.write('line1\n')
#     data.write('line2\n')

# -----------------------------------------

# path = 'file.txt'   # чтение данных из файла
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()        # закрывается подключение, прерывается работа с файлом

# -----------------------------------------

# import hello as h   # позволяет обращаться к файлу с функцией и не указывать функции в том же файле с кодом, as h - переименование файла в "h"
# print(h.f(1))

# -----------------------------------------

# def new_string(symbol, count):      # функция умножает строку на число в том числе
#     return symbol * count

# print(new_string('!', 5))           # резульатат: !!!!!
# print(new_string('!'))              # выдаст ошибку, так как не указано значение переменной count
# Если задать в функции (def new_string(symbol, count = 3):) значение count сразу, то ввод второй переменной не потребуется

# -----------------------------------------

# def concatenatio(*params):
#     res: str = ''
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w'))
# print(concatenatio('a', '1', 'd', '2'))
#       print(concatenatio(1, 2, 3, 4)) # TypeError. Можно указать или res: int = 0 или res = 0. Тогда функция посчитает в данном случае сумму всех элементов переданных переменных

# -----------------------------------------

# ФУНКЦИИ
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + feb(n-2)

# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)     # 1 1 2 3 4 5 8 21 34

# -----------------------------------------

# СЛОВАРИ
# dictionary = {}
# dictionary = \
#  {
#  'up': '↑',
#  'left': '←',
#  'down': '↓',
#  'right': '→'
#  }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←

# for k in dictionary.keys():     # обращается только к ключам
#     print(k)
# for k in dictionary.values():   # обращается к значениям
#     print(k)

# print(dictionary['up'])
# dictionary['up'] = 'up'     # заменяет элемент в словаре
# print(dictionary['up'])

# -----------------------------------------

# МНОЖЕСТВА
# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a \
#  .union(b) \
#  .difference(a.intersection(b))

# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8}) - неизменяемое множество

# -----------------------------------------
# СПИСКИ
list1 = [1,2,3,4,5]
print(list1.pop(2))     # 2 - это индекс того значения, которое нужно удалить
print(list1.insert(2, 11))      # 2 - индекс, 11 -значение, которое будет вставлено
print(list1.append(12))         # добавляет элемент в конец списка
print(list1)

# print(list1)      # демонстрирует принцип работы .pop
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)

