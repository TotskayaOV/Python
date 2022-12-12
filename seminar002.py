# Напишите программу, которая на вход принимает 5 чисел 
# и находит максимальное из них.

#ввод данных для первого и второго решений:
# num1 = int(input('Введите первое число:'))
# num2 = int(input('Введите второе число:'))
# num3 = int(input('Введите третье число:'))
# num4 = int(input('Введите четвертое число:'))
# num5 = int(input('Введите пятое число:'))

# ПЕРВОЕ РЕШЕНИЕ:
# if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
#     print (f'{num1} максимальное')
# elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
#     print (f'{num2} максимальное')
# elif num3 > num1 and num3> num2 and num3 > num4 and num3 > num5:
#     print (f'{num3} максимальное')
# elif num4 > num1 and num4> num2 and num4 > num3 and num4 > num5:
#     print (f'{num4} максимальное')
# else:
#     print (f'{num5} максимальное')


#ВТОРОЕ РЕШЕНИЕ:
# my_max = num1
# if my_max<num2:
#    my_max = num2
# if my_max<num3:
#    my_max = num3
# if my_max<num4:
#    my_max = num4
# if my_max<num5:
#    my_max = num5
# print(my_max)


#ТРЕТЬЕ РЕШЕНИЕ
numbers = []
for i in range(1,6):
    numbers.append(int(input(f'Введите элемент под номером {i}: ')))
    # append добавляет данные в конец массива
print(numbers)
print(max(numbers))