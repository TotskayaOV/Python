# Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве.
import math
coordinate1 = int(input('Введите координату Х первой точки: '))
coordinate2 = int(input('Введите координату Y первой точки: '))
coordinate3 = int(input('Введите координату Х второй точки: '))
coordinate4 = int(input('Введите координату Y второй точки: '))

result = ((coordinate1 - coordinate3) ** 2 + (coordinate2 - coordinate4) ** 2)**0.5
print(round(result, 3))