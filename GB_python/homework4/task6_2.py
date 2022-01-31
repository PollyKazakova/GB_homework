'''
Реализовать два небольших скрипта:
- итератор, генерирующий целые числа, начиная с указанного;
- итератор, повторяющий элементы некоторого списка, определённого заранее.
'''

from itertools import cycle
from sys import argv

script_name, stop_number = argv

list = [1, 10, 15, 'A', 89, 'B', 101, 'C', -16, 23.1]
i = 0
for el in cycle(list):
    if i >= int(stop_number):
        break
    print(el)
    i += 1
