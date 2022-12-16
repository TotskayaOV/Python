# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num1 = int(input('Введите число N: '))
result = [1]
temp_num = 1
for i in range(1, num1 + 1):
    result.append(i * temp_num)
    temp_num = result[i - 1]
print(result)

