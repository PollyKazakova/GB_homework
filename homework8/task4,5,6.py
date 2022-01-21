'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
'''

class Storage:

    def __init__(self, name, price, amount, num_list, *args):
        self.name = name
        self.price = price
        self.amount = amount
        self.num_list = num_list
        self.storage = []
        self.storage_total = []
        self.module = {'Модель оргтехники': self.name, 'Цена за единицу': self.price, 'Количество': self.amount}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.amount}'

    def recip(self):
        try:
            unit = input(f'Введите название товара: ')
            unit_price = int(input(f'Введите цену за единицу товара: '))
            unit_amount = int(input(f'Введите количество единиц товара: '))
            unique = {'Модель устройства': unit, 'Цена за ед. продукции': unit_price, 'Количество товара': unit_amount}
            self.module.update(unique)
            self.storage.append(self.module)
            print(f'Текущий список -\n {self.storage}')
        except:
            return f'Ошибка ввода данных!'

        step = input(f'Для выхода введите Q, для продолжения ввода - Enter')
        if step.upper() == 'Q':
            self.storage_total.append(self.storage)
            print(f'Весь склад -\n {self.storage_total}')
            return f'Выход'
        else:
            return Storage.recip(self)


class Printer(Storage):
    def to_print(self):
        return f'to print something {self.num_list} times'


class Scanner(Storage):
    def to_scan(self):
        return f'to scan something {self.num_list} times'


class Copier(Storage):
    def to_copy(self):
        return f'to copy something {self.num_list} times'


unit_1 = Printer('Canon', 4200, 12, 7)
unit_2 = Scanner('Epson', 2700, 6, 13)
unit_3 = Copier('Mustek', 7000, 2, 10)
print(unit_1.recip())
print(unit_2.recip())
print(unit_3.recip())
print(unit_1.to_print())
print(unit_2.to_scan())
print(unit_3.to_copy())
