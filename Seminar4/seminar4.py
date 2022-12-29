# Создайте словарь заданный по формуле 3n+1, где n - это ключ, а формула - значение

my_dict = {}
num = int(input('Введите целое число: '))
for n in range(1, num+1):
    my_dict[n] = 3 * n + 1

print(my_dict)