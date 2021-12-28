'''
Реализовать два небольших скрипта:
- итератор, генерирующий целые числа, начиная с указанного;
- итератор, повторяющий элементы некоторого списка, определённого заранее.
'''

from itertools import count
from sys import argv

script_name, min_int, max_int = argv

for el in count(int(min_int)):
    if el > int(max_int):
        break
    else:
        print(el)
