# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def del_repeat(new_list):
    norepeat_list = []
    for i in new_list:
        while True:
            if i in norepeat_list:
                break
            else:
                norepeat_list.append(i)
    return norepeat_list

def main():
    my_list = [2, 1, 5, 3, 7, 2, 1, 3, 2, 9]
    my_list = del_repeat(my_list)
    print(my_list)


if __name__ == "__main__":     # точка входа
    main()



#другое решение в котором где-то что-то не работает
# def del_repeat(new_list):
#     step_len = len(new_list)-1
#     for i in range(0, step_len):
#         temp_num = int(new_list.pop(i))
#         while _ in new_list:
#             if temp_num in new_list:
#                 new_list = new_list.remove(temp_num)
#                 step_len = step_len - 1
#         new_list = new_list.insert(i, temp_num)
        
#     return new_list


my_list = [2, 1, 5, 3, 7, 2, 1, 3, 2, 9]
my_list = del_repeat(my_list)
print(my_list)