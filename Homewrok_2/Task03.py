# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random 
# для и получения случайного int

import random
my_list = [4, 5, 1, 7, 9, 2, 3]

for z in range(len(my_list)):
    i = random.randint(0, len(my_list)-1)
    temp = my_list[i]
    x = random.randint(0, len(my_list)-1)
    my_list[i] = my_list[x]
    my_list[x] = temp
else:
    print(my_list)