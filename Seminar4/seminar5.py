my_string = '   Python is the best language in the world\n'
my_list = ['1', '2', '3', '4', '5', '6', '7', '8']
# my_string = my_string.split('i')

# my_string = my_string.replace('i', '@')
print(my_string.strip())    # убирает служебные символы
print(' '.join(my_list))
print(my_string.startswith('Pyt'))
print(my_string.endswith('rld'))
print(my_string)