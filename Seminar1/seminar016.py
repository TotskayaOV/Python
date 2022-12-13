num_day = input('Введите номер дня недели: ')
while num_day not in  ('1', '2', '3', '4', '5', '6', '7') and num_day != 'exit':
    num_day = input('Введите номер дня недели: ')
   
if num_day.isdigit():
    num_day = int(num_day)
    print('Номер дня недели', num_day)

