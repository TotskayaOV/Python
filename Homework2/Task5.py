# Реализуйте алгоритм перемешивания списка.
import random

# Создаем список с заданными элементами и пустой списко i_list, который
# будет заполняться рандомными занчениями от 0 до длинна созданного списка минус 1
# my_list = [4, 5, 1, 7, 9, 2, 3]
# i_list = []
# for i in range(len(my_list)):
#     i_list.append(random.randint(0, len(my_list)-1))

# # Создаем переменную y с рандомным значением от 0 до длинны списка my_list минус 1
# # для того, чтобы первый элемент в цикле for был также случайным
# # В цикле for проходим по списку i_list получая из него значение индекса списка my_list
# # По окончанию цикла выводим результат на экран

# y = random.randint(0, len(my_list)-1)
# for z in range(len(i_list)):
#     temp = my_list[y]
#     y = i_list[z]
#     my_list[y] = temp
# else:
#     print(my_list)

def list_shuffle(my_list: list):
    shuffled_list = []
    temp_list = my_list.copy()

    for _ in range(len(my_list)):
        position = random.randint(0, len(temp_list) - 1) # задается случайный индекс 
        shuffled_list.append(temp_list.pop(position)) # вырезает элемент на позиции с выбранным индексом и вернул его в новый лист
    return shuffled_list

print(list_shuffle([4, 5, 1, 7, 9, 2, 3]))