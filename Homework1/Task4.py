# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y)

quarter = input('Введите номер четверти: ')
while quarter not in  ('1', '2', '3', '4') and quarter != 'exit':
    quarter = input('Введите номер дня недели: ')
   
if quarter.isdigit():
    quarter = int(quarter)
    if quarter == 1:
        print(f'{quarter} четверть -> X > 0; Y > 0')
    elif quarter == 2:
        print(f'{quarter} четверть -> X < 0; Y > 0')
    elif quarter == 3:
        print(f'{quarter} четверть -> X < 0; Y < 0')
    else:
        print(f'{quarter} четверть -> X > 0; Y < 0')
