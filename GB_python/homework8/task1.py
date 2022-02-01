'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''

class Date:

    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def convert_to_int(cls, date):
        res_date = []
        for i in date.split(sep='-'):
            res_date.append(i)
        return int(res_date[0]), int(res_date[1]), int(res_date[2])


    @staticmethod
    def validation(day, month, year):
        print('Запущена проверка введенных данных:')
        if 1 <= day <= 31:
            print('Введено корректное значение дня!')
        else:
            print('Введено некорректное значение дня!')
        if 1 <= month <= 12:
            print('Введено корректное значение месяца!')
        else:
            print('Введено некорректное значение месяца!')
        if 1 <= year <= 2022:
            print('Введено корректное значение года!')
        else:
            print('Введено некорректное значение года!')


print(Date.convert_to_int('25-06-1996'))
print(Date.validation(16, 14, 2001))