# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

Number = input("Введите вещественное число: ")
sum1 = 0
for i in Number:
    if i.isdigit():
        sum1 += int(i)
print(sum1)

# Решение без isdigit
# def split(s):                         # функция делит строку на символы
#     return [char for char in s]

# numbers_user = input('Введите число: ')
# my_list = split(numbers_user)
# for i in my_list:                     # удаляем (-, ., ,) из массива, если они есть
#     if ',' in my_list:
#         my_list.remove(',')
#     elif '.' in my_list:
#         my_list.remove('.')
#     elif '-' in my_list:
#         my_list.remove('-') 
#     else:
#         break
# sum = sum(map(int, my_list))          # преобразует каждый элемент списка в целое число и суммирует
# print(sum)


# # Решение не через строку:
# x = float(input())
# count = 0
# while x%1 != 0:
#     x = x * 10
#     count += 1
# else:
#     my_list = []
#     while x != 0:
#         b = int(x%10)
#         my_list.append(b)
#         x = int(x / 10)
# print(sum(my_list))