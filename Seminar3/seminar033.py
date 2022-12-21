# напишите программу которая определит позицию второго вхождения строки в  списке, либо сообщит что ее нет

# my_list = ['qwe', 'asd', 'zxc', 'qwe', 'ertqwe']
# str_find = 'qwe'
# count = 0
# for i in range(len(my_list)):
#     if str_find == my_list[i]:
#         count+=1
#         if count == 2:
#             print(f'in {my_list} "{str_find}" position - {i}')
#             break
# else:
#     print(-1)

#-------------------------------------------

#  с помощтю индекс метода

my_list = ['qwe', 'asd', 'zxc', 'qwe', 'ertqwe']
my_str = 'qwe'
if my_str in my_list:
    index_str = my_list.index(my_str)
    if my_str in my_list[index_str + 1:]:
        print(my_list.index(my_str, index_str + 1))
    else:
        print(-1)

#-------------------------------------------

# my_list = ['qwe', 'asd', 'zxc', 'qwe', 'ertqwe']
# my_str = 'qwe'

# if my_list.count(my_str) > 1:
#     index_str = my_list.index(my_str)
#     print(my_list.index(my_str, index_str + 1))
# else:
#     print(-1)