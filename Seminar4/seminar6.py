# equation = 3 * x ** 2 + 5 * x - 6 = 0
#  Найдите корни квадртаного уравнения Ах**2 + Вх + С = 0 с помощью математических формул квадратного уравнения

equation = 'x**2 - 4*x - 5 = 0'
equation = equation.replace('**2', '').replace('*x', '').replace(' = 0', '').replace('- ', '-').replace(' + ', ' ').replace('x', '1').split(' ')
# if 'x' in equation:
#     equation = equation.replace('x', '1')
num_a = int(equation[0])
num_b = int(equation[1])
num_c = int(equation[2])
print(equation)
discrim = num_b ** 2 - 4 * num_a * num_c

if discrim < 0:
    print('Нет корней')
elif discrim == 0:
    print((-(num_b / (2 * num_a))))
else:
    print(f'1 корень: {((-num_b) + discrim ** 0.5)/ (2 * num_a)} ')
    print(f'2 корень: {((-num_b) - discrim ** 0.5)/ (2 * num_a)} ')