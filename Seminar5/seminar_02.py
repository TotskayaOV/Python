# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# *Пример:* 
# 1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

num_list = [1, 5, 2, 3, 4, 6, 1, 7]  
print(num_list, end=' => ')

min_num = num_list[0]

for i in range(len(num_list)):
    order_list = []
    order_list.append(num_list[i])
    min_num = num_list[i] 
    for j in range(i,len(num_list)-1):
        if num_list[j] > min_num:
            min_num = num_list[j]
            order_list.append(num_list[j])
    if len(order_list) > 1:
        print(order_list, end=' ')
