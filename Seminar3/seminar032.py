# Задайте список. Напишите программу, которая определит, присутствует ли в заднном списке строк некое число

# my_list = ['2', '43', '5', '331', '91', '35', '79', '53']
# num1 = input('Numbers: ') 


# for i in my_list:
#     if num1 == i:
#         print('yes')
#         break
# else:       # выведется только если for отработает полностью
#     print('no')


#Решение через функцию

def chek(stringlist: list, n: str) -> bool:
    for i in stringlist:
        if n == i:
            return True
            break
    else:
        return False

my_list = ['2', '43', '5', '331', '91', '35', '79', '53']
num1 = input('Numbers: ')
if chek(my_list, num1):
    print('yes')
else:
    print('no')