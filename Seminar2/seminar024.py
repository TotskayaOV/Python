# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вохождений одной строки в другой

string_user1 = set(input('Введите первую строку'))
string_user2 = set(input('Введите вторую строку'))

string_dubl = string_user1.intersection(string_user2)
print(string_dubl)