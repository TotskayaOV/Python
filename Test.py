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
   
# path = 'file.txt'   # чтение данных из файла
# data = open(path, 'r')
# my_list = []
# for line in data:
#     line = line.replace('\n', '')
#     my_list.append(line)
# data.close()
# str12 = ''.join(my_list)
# # for i in str12:
# #     if '\n' in str12:
# #         str12.remove('\n')
# #     else:
# #         break

# # my_list = my_list.replace('\n', '')
  
# print(my_list)
# print(str12)

# content = path.read
# element_num = content(position_num)
# data = open(path, 'r')
# element_num = int(position_num)
# print(element_num)

# def converting_list(num1):
#     i_list = []
#     while num1 != 0:
#         b = int(num1%10)
#         i_list.append(b)
#         num1 = int(num1 / 10)
#     else:
#         return i_list


# x = float(input())
# count = 0
# while x%1 != 0:
#     x = x * 10
#     count += 1
# else:
#     my_list = []
#     while x != 0:
#         b = int(x%10)
#         my_list.append(b)
#         x = int(x / 10)
# print(sum(my_list))
           
         
# my_list = []

# while x != 0:
#     b = x%10
#     my_list.append(b)
#     x = int(x / 10)
# else:
#     print(my_list)


# a = 82 // 3 ** 2 % 7
# print(a)

# numbers = int(input())
# a = numbers % 10
# b = (numbers//10) % 10
# c = (numbers//100) % 10
# d = numbers//1000
# print(f'Цифра в позиции тысяч равна {d}')
# print(f'Цифра в позиции сотен равна {c}')
# print(f'Цифра в позиции десятков равна {b}')
# print(f'Цифра в позиции единиц равна {a}')

# num1 = 54321
# x = 10000
# while num1 != 0:
#     print(*str(num1), sep = ' ')
#     num1 = int(num1%x)
#     x = x/10

# n = 5
# for i in range(n, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=' ')
#     print()

import array as arr
numbers = arr.array('i',[10,20,30])
print(type(numbers))
print(type(numbers[0]))