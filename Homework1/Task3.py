# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

coordinate1 = int(input('Введите координату Х: '))
coordinate2 = int(input('Введите координату Y: '))

if coordinate1 > 0:
    if coordinate2 > 0:
        print(f'x = {coordinate1}; y = {coordinate2} -> 1 четверть')
    else:
        print(f'x = {coordinate1}; y = {coordinate2} -> 4 четверть')
else:
    if coordinate2 > 0:
        print(f'x = {coordinate1}; y = {coordinate2} -> 2 четверть')
    else:
        print(f'x = {coordinate1}; y = {coordinate2} -> 3 четверть')

