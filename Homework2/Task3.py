# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

num1 = int(input('Введите число n:'))

my_dict = {}
for i in range(1, num1+1):
    my_dict[i] = round((1 + 1 / i)**i, 2)

print(f' для n = {num1}: {my_dict} \n Сумма:  {round(sum(my_dict.values()), 2)}')