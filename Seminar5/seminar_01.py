# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие 
# A[i] - 1 = A[i-1]. Найдите это число.

# my_file = open("Seminar5/new_file.txt", "w+")
# my_file.write("Привет, файл!")
# my_file.close()

with open(r'Seminar5/new_file.txt', 'w', encoding = 'UTF-8') as f:
        f.write('1 2 3 4 5 6 8 9 10')

path = 'Seminar5/new_file.txt'   # чтение данных из файла
data = open(path, 'r')

for line in data:
    num_row = list(map(int, line.split()))
data.close()    
print(num_row)

for i, elem in enumerate(num_row[:-1]):
    if elem + 1 != num_row[i+1]:
        print(elem + 1)
