# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

user_num = input("Введите вещественное число: ")
sum1 = 0
for i in user_num:
    if i.isdigit():
        sum1 += int(i)
print(sum1)
