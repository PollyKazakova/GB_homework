'''
Программа запрашивает у пользователя строку чисел, разделённых пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''

def my_sum():
    '''
    Функция, выводящая сумму введенных через пробел чисел
    '''

    sum_res = 0
    while True:
        number = input('Введите строку чисел, разделенных пробелами. Для выхода из программы нажмите Q: ').split()
        for el in number:
            if el.upper() == 'Q':
                return f'Финальная сумма введенных значений равна: {sum_res}'
                break
            else:
                sum_res = sum_res + int(el)
        print(f'Текущая сумма введенных значений равна: {sum_res}')


print(my_sum())