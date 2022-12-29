import s_my_modul


my_list = input('Введите числа через пробел: ').split()

print(*s_my_modul.find_min_max(my_list))