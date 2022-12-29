# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import Task3_repeatmodul

num = int(input("Введите число: "))
i = 2  
my_list = []
temp = num
while i <= num:
    if num % i == 0:
        my_list.append(i)
        num //= i
        i = 2
    else:
        i += 1

print(f"Список простых множителей числа {temp}: {Task3_repeatmodul.del_repeat(my_list)}")

