'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''
import traceback

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))

class DivOnZero(Exception):

    def incorrect_div(num_1, num_2):
        return num_1 / num_2
    try:
        res = incorrect_div(num_1, num_2)
        print(f'Результат деления {num_1} на {num_2}: {res}')
    except Exception as e:
        print('Программа завершилась с ошибкой:\n', traceback.format_exc())
