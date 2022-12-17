# def f (list_1):
#     result1 = not sum(list_1)
#     result2 = not list_1[0] and not list_1[1] and not list_1[2]
#     result = result1 == result2
#     return result


# predicators = [False, False, False]
# result = f(predicators)
# if result == True:
#     predicators = [True, False, False]
#     result = f(predicators)
#     if result == True:
#         predicators = [False, True, False]
#         result = f(predicators)
#         if result == True:
#             predicators = [False, False, True]
#             result = f(predicators)
#             if result == True:
#                 predicators = [True, True, False]
#                 result = f(predicators)
#                 if result == True:
#                     predicators = [True, False, True]
#                     result = f(predicators)
#                     if result == True:
#                         predicators = [False, True, True]
#                         result = f(predicators)
#                         if result == True:
#                             predicators = [True, True, True]
#                             result = f(predicators)
#                             if result == True:
#                                 print('Утверждение истинно')
# else:
#     print('Утверждение ложно')

# with open('file.txt', 'w') as data:
#     data.write('line1\n')
#     data.write('line2\n')


# position_num = 3
# path = 'file.txt'   # чтение данных из файла
# my_list = []
# with True:
#     i = path.read()
#     if not i:
#         break
#     print(i)
   
path = 'file.txt'   # чтение данных из файла
data = open(path, 'r')
my_list = []
for line in data:
    line = line.replace('\n', '')
    my_list.append(line)
data.close()
str12 = ''.join(my_list)
# for i in str12:
#     if '\n' in str12:
#         str12.remove('\n')
#     else:
#         break

# my_list = my_list.replace('\n', '')
  
print(my_list)
print(str12)

# content = path.read
# element_num = content(position_num)
# data = open(path, 'r')
# element_num = int(position_num)
# print(element_num)