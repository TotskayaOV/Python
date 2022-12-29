# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def select_koef(equation: str):
    new_equation = equation.replace(' ', '').replace('=0', '').replace('+', ' ').replace('-', ' -')
    new_equation = new_equation.split()
    new_list = []
    for item in new_equation:
        if item.startswith('x'):
            new_list.append(1)
        elif item.startswith('-x'):
            new_list.append(-1)
        else:
            new_list.append(item.split('*x')[0])
    return(new_list)


def f1(name_file):
    with open(name_file) as data:
        return data.read()
    

first_string = select_koef(f1('1mn_file.txt'))
too_string = select_koef(f1('2mn_file.txt'))
num1 = int(first_string[0])+int(too_string[0])
num2 = int(first_string[1])+int(too_string[1])
num3 = int(first_string[2])+int(too_string[2])

if num1 == 1 or num1 == 0:
    result_string = 'x ** 2'
elif num1 < -1 or num1 > 1:
    result_string = str(num1) + 'x ** 2'
else:
    result_string = '- x ** 2'

if num2 < -1:
    result_string += str(num2) + '*x'
elif num2 == 1 or num2 == 0:
    result_string += ' + x'
elif num2 == -1:
    result_string += ' - x'
else:
    result_string += ' + ' + str(num2) +' * x '

if num3 < 0:
    result_string += str(num3)
elif num3 > 0:
    result_string += '+' + str(num3)

with open('result_file.txt', 'w') as data:
    data.write(result_string)
