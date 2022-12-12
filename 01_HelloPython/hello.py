# print('Hello World!')

# print() – отвечает за вывод данных
# input() – отвечает за ввод данных


#f = [1,2,3,4]
#is_odd = not f[1] % 2 
#print(is_odd)
#is_odd2 = f[0] % 2 == 0
#print(is_odd2)

# print('Введите а');
# a = input()
# print('Введите b');
# b = input()
# print(a, b)
# print('{} -- {}'.fotmat(a, b))

# a = int(input('Введите \nа: '))
# b = int(input('Введите \nb: '))
# c = a + b
# print('{} + {} = {}'.format(a, b, c))

# iter = 2
# iter += 3     # iter = iter + 3
# iter -= 4     # iter = iter - 4
# iter *= 5     # iter = iter * 5
# iter /= 5     # iter = iter / 5
# iter //= 5    # iter = iter // 5
# iter %= 5     # iter = iter % 5
# iter **= 5    # iter = iter ** 5

#Управляющие конструкции 
#if, if-else

# a = int(input('a = ')) #присваивание вместе со строкой приглашением
# b = int(input('b = ')) #присваивание вместе со строкой приглашением
# if a > b:
#     print(a)
# else:
#     print(b)

# original = 23
# inverted = 0
# while original != 0:
#  inverted = inverted * 10 + (original % 10)
#  original //= 10
# else:
#  print('Пожалуй')
#  print('хватит )')
# print(inverted)


# username = input('Введите имя: ')
# if username == 'Маша':
#  print('Ура, это же МАША!')
# elif username == 'Марина':
#  print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#  print('Ильнар - топ)')
# else:
#  print('Привет, ', username)


# RANGE

# r = range(5)           # range(0, 5)
# r = range(2, 5)        # range(2, 5)
# r = range(-5, 0)       # range(-5, 0)
# r = range(1, 10, 2)    # range(1, 10, 2)
# r = range(100, 0, -20) # range(100, 0, -20)


# line = ""
# for i in range(5):
#  line = ""
#  for j in range(5):
#   line += "*"
# print(line)


#СПИСКИ
# numbers = [1, 2, 3, 4, 5]
# print(numbers)            # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers)            # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers)            # [10, 2, 3, 4, 5]
# for i in numbers:
#  i *= 2
#  print(i)                 # [20, 4, 6, 8, 10]
# print(numbers)            # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#  print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент


# Функции
# def f(x):
#  return x**2


def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
arg = int(input('x = '))
print (f(arg))