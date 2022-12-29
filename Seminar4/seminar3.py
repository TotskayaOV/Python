# Задайте 2 числа. Напишите программу которая найдет наименьшее общее кратное из этих двух чисел


num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
max_num = max(num1, num2)
for i in range(max_num, num1 * num2 + 1, max_num):
    if i % num1 == 0 and i % num2 == 0:
        print(f'Для {num1} и {num2} нок = {i}')
        break