# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

num1 = 8
my_list = [0, 1]
my_list2 = []
if num1 == 0:
    my_list = [0]
    print(f'для числа = 0 список будет выглядеть так: {my_list}')
else:
    for i in range(1, num1):
         my_list.append(my_list[i]+my_list[i-1])
    for y in range(1, num1+1):
        my_list2.append(((-1)**(y+1))*my_list[y])
    my_list2.reverse()
    print(f'для числа = {num1} список будет выглядеть так: {my_list2 + my_list}')