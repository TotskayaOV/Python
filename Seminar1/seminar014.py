# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#     *Примеры:*
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

# Ввод как строка
# num = input('Введите число: ')
# print(num, end=' -> ')
# if '.' in num:
#     print(num[num.find('.')+1])
# elif ',' in num:
#     print(num[num.find(',')+1])
# else:
#     print('нет')    


num = float(input('Введите число: '))
if not num % 1:
    print ('нет')
else:
    num = int(num * 10 % 10)
    print(num) 

# n = 25.31
# print(n)
# n = n % int(n)
# n = n * 10
# n = n // int(n)
# print(n)

# num = input('Введите дробное число: ')
# if num.isdigit():
#     print('нет')
# else:
#     num = int(float(num)*10 % 10)
#     print(num)
