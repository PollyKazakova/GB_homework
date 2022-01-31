'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

from random import randint

with open('sum.txt', 'w+', encoding='utf-8') as f:
    f.write(' '.join([str(randint(1, 10000)) for _ in range(100000)]))
    f.seek(0)
    print(f'Сумма чисел в файле равна: {sum(map(int, f.readline().split()))}')
