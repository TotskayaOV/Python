# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def del_repeat(new_list):
    norepeat_list = []
    for i in new_list:
        while True:
            if i in norepeat_list:
                break
            else:
                norepeat_list.append(i)
    return norepeat_list

def main():
    my_list = [2, 1, 5, 3, 7, 2, 1, 3, 2, 9]
    my_list = del_repeat(my_list)
    print(my_list)


if __name__ == "__main__":     # точка входа
    main()
