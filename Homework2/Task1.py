# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def split(s):                         # функция делит строку на символы
    return [char for char in s]

numbers_user = input('Введите число: ')
my_list = split(numbers_user)
for i in my_list:                     # удаляем (-, ., ,) из массива, если они есть
    if ',' in my_list:
        my_list.remove(',')
    elif '.' in my_list:
        my_list.remove('.')
    elif '-' in my_list:
        my_list.remove('-') 
    else:
        break
sum = sum(map(int, my_list))          # преобразует каждый элемент списка в целое число и суммирует
print(sum)