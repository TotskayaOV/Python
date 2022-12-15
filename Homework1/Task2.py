# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
 
for x in 1, 0:
    for y in 1, 0:
        for z in 1, 0:
            print(f'x = {x} y = {y} z = {z}', end=' -> ')
            print(not (x and y and z) == (not x) or (not y) or (not z))


# Второй (не наглядный вариант)
# for x in True,False:
#     for y in True,False:
#         for z in True,False:
#             if (not (x and y and z) == (not x) or (not y) or (not z)):
#                 result = 'Утверждение истинно'
#             else:
#                 result = 'Утверждение ложно'
# print(result)

# Третий вариант (простой как топор, но проверяет все железобетонно)
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
