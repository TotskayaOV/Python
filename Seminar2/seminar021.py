# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

# Первое решение (для случайных чисел):
# import random

# num1 = int(input('Введите число: '))
# for num2 in range(num1):
#     print(random.randint(1, 100), end=' ')

# Второе решение:
num1 = int(input('Введите число: '))

for degree in range(num1):
    print((-3)**degree, end=' ')