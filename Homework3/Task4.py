#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

x = 45

my_list = []
temp = x//2

while temp > 0:
    my_list.append(x - temp * 2)
    x = temp
    temp = x//2
if x != 0:
    my_list.append(1)
else:
    my_list = [0]
my_list.reverse()
print("".join(map(str, my_list)))