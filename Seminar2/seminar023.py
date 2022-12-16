# Напишите программу, которая будет на вход принимать 
# число N и выводить числа от -N до N
# *Примеры:* 
# при 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5


num1 = int(input('Введите число N:'))
print(f'при {num1} ->', end= ' ')
if num1 < 0:
    num1 = num1 * (-1)
my_list = []
for i in range(-num1, num1+1):
    my_list.append(i)
print(*my_list, sep=', ')

# num1 = int(input('Введите число N:'))
# print(f'при {num1} ->', end= ' ')
# if num1 < 0:
#     num1 = num1 * (-1)
# for i in range(-num1, num1+1):
#     print(i, end = ' ')

for i in range(num1 + abs(num1)//num1, abs(num1)//num1):
    my_list.append(i)
