'''
Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
'''

my_list = list(input('Введите элементы Вашего списка: '))
max_index = len(my_list) - 1
i = 0
j = 1
new_list = list()

if (len(my_list) % 2) == 0:
    while j <= max_index:
        new_list.append(my_list[j])
        new_list.append(my_list[i])
        i += 2
        j += 2
    print(new_list)
else:
    while j < max_index:
        new_list.append(my_list[j])
        new_list.append(my_list[i])
        i += 2
        j += 2
    new_list.append(my_list[max_index])
    print(new_list)
