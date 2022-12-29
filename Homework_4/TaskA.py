# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100) многочлена 
# и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

power_num = int(input('Введите значение натуральной степени: '))

my_dict = {}        
for i in range(0, power_num+1):
    my_dict[i] = random.randint(-100, 100)
items = list(my_dict.items())
my_dict2 = {k: v for k, v in reversed(items)}

my_list = []
for key, value in my_dict2.items():
    my_list.append(str(value))
    my_list.append('* x **')
    my_list.append(str(key))
    my_list.append('+')

for i in range(len(my_list)-1):
    if my_list[i].startswith('-') and i != 0:
        del my_list[i-1]
        my_list.insert(i-1, '0')
        if my_list[i] == '-1':
            del my_list[i]
            my_list.insert(i, '-')
    elif i == 0 and (my_list[i] == '1' or my_list[i] == '0'):
        del my_list[i+1]
        my_list.insert(i+1, 'x **')
del my_list[len(my_list)-3:len(my_list)]

strin = ' '.join(my_list)
pre_result = strin.replace('**', '^').replace('0', '').replace(' ^ ', '^').replace('-', '- ').replace(' * ', '*').replace('1*x', 'x').replace('  ', ' ').replace(' *x', ' x') + str(' = 0')
result = pre_result.replace(' +  = 0', ' = 0').replace(' -  = 0', ' = 0').replace('x^1', 'x').replace('1 x', 'x')

with open('result_taskA.txt', 'a') as data:
    data.writelines(f'k={power_num} => {result}\n')
