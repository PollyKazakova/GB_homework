'''
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция вызывается следующим образом: for el in fact(n).
Она отвечает за получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
'''

from math import factorial
from itertools import count

def gen_factorial():
    '''
    Функция, возвращающая факториал числа
    '''

    for el in count(1):
        yield factorial(el)


generator = gen_factorial()

x = 0
for i in generator:
    if x <= 30:
        print(f'Факториал числа {x} равен: {i}')
        x += 1
    else:
        break
