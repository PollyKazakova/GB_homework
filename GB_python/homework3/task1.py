'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

def division_calculation(var1, var2):
    '''
    Функция, принимающая два числа (позиционные аргументы) и выполняющая их деление
    '''

    try:
        division = var1 / var2
        print(f'Результат деления Ваших чисел: {round(division, 3)}')
    except ZeroDivisionError as e:
            print('Делитель не может быть равен нулю!')


var1 = int(input('Введите первое число: '))
var2 = int(input('Введите второе число: '))

print(division_calculation(var1, var2))