# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import random
# Получаем все строки из файла, убирая перенос на следующую строку функцией .replace,
# Добавляем все полученные элементы во временный список fail_list.
# Возвращаем элемент из списка под индексом position_num (элемент строки)

def f1(position_num):
    path = 'file.txt'   # чтение данных из файла
    data = open(path, 'r')
    fail_list = []
    for line in data:
        line = line.replace('\n', '')
        fail_list.append(line)
    data.close()
    return fail_list[position_num]
    


num1 = int(input('Введите число N: '))
if num1 < 12:
    num2 = int(input(f'Введите номер строки (от 1 до {num1}): ')) - 1
    num3 = int(input(f'Введите номер второй строки (от1 до {num1}): ')) - 1
else:
    num2 = int(input('Введите номер строки (от 1 до 11): ')) - 1
    num3 = int(input('Введите номер второй строки (от 1 до 11): ')) - 1
my_list = []
for num4 in range(num1):
    my_list.append(random.randint(-num1, num1+1))
multiplier1 = int(f1(num2))
multiplier2 = int(f1(num3))
result = my_list[multiplier1] * my_list[multiplier2]
print(result)
print(my_list)

