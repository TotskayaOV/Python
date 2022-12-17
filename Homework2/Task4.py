# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
import random
def f1(position_num):
    path = 'file.txt'   # чтение данных из файла
    content = path.readlines()
    element_num = content(position_num)
    # data = open(path, 'r')
    # element_num = int(position_num)
    return element_num
    

num1 = int(input('Введите число N: '))
my_list = []
for num2 in range(num1):
    my_list.append(random.randint(-num1, num1))
multiplier1 = f1(3)
print(multiplier1)
print(my_list)

