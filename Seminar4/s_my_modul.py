# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качеств символа разделителя используйте пробел

# list_num = input(': ').split()  # метод split разбирает строку по пробелам, если поставить в скобках другой символ, то он разберет строку по этому символу
# print(list_num)
# list_num = list(map(int, list_num)) #  перевод список строк в список чисел
# print(max(list_num), min(list_num))


def find_min_max(list_num):
    min_num = int(list_num[0])
    max_num = int(list_num[0])
    for num in list_num:
        num = int(num)
        if max_num < num:
            max_num = num
        elif min_num > num:
            min_num = num
    return max_num, min_num


def main(): # основной код
    list_num = input('Введите числа через пробел: ').split()  # метод split разбирает строку по пробелам, если поставить в скобках другой символ, то он разберет строку по этому символу
    print(*find_min_max(list_num))

if __name__ == "__main__":     # точка входа
    main()
