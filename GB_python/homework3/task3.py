'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента и
возвращает сумму наибольших двух аргументов.
'''

def my_func(var1, var2, var3):
    '''
    Функция, возвращающая сумму двух наибольших аргументов
    '''

    list = [var1, var2, var3]
    list.sort()
    sum = list[-1] + list[-2]
    return(sum)


print(my_func(8, 18, -3))