# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def split(s):
    return [char for char in s]

numbers_user = input('Введите число: ')
my_list = split(numbers_user)
my_list.remove(',') 
sum = sum(map(int, my_list))
print(sum)