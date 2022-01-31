'''
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
'''

my_list = [7, 5, 3, 3, 2, 1]
new_int = int(input('Введите новый элемент рейтинга: '))
new_index = len(my_list)
i = 1
while i < len(my_list):
    if new_int > my_list[len(my_list) - i]:
        new_index = len(my_list) - i
    i += 1
if new_int > my_list[0]:
    new_index = 0
my_list.insert(new_index, new_int)
print(my_list)
