'''
Реализовать класс Stationery (канцелярская принадлежность).

определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return('Запуск отрисовки')

class Pen(Stationery):

    def draw(self):
        return (f'Инструмент для отрисовки скетча - {self.title}.')

class Pencil(Stationery):

    def draw(self):
        return(f'Начинается мастер-класс. Инструмент - {self.title}.')

class Handle(Stationery):

    def draw(self):
        return(f'{self.title} - лучший инструмент для того, чтоб учиться рисовать.')


#Проверка работоспособности кода
pen_1 = Pen('Pilot')
pencil_1 = Pencil('Koh-i-Noor')
handle_1 = Handle('Mazeratti')
print(pen_1.draw(), pencil_1.draw(), handle_1.draw(), sep=''\n')
