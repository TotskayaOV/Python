# Напишите программу, которая принимает на вход два числа 
# и проверяет, является ли одно число квадратом другого.

num1, num2 = int(input("введите первое число: ")), int(input("введите второе число: "))
print(f'{num1}, {num2} ->', end= ' ') # end оставляет курсор на той же строке
if num1 ** 2 == num2 or num2 ** 2 == num1:
    print("да")
else:
    print("нет")