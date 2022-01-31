'''
Реализуйте базовый класс Car.

у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
'''

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.colr = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return(f'Автомобиль {self.name} поехал')

    def stop(self):
        return(f'Автомобиль {self.name} остановился')

    def turn(self, direction):
        self.direction = direction
        return(f'Автомобиль {self.name} повернул {direction}')

    def show_speed(self):
        return (f'Автомобиль {self.name} движется со скоростью {self.speed} км/ч')

    def police_return(self):
        if self.is_police == True:
            return 'Это полицейский автомобиль'
        else:
            return 'Это обычный автомобиль'

class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return(f'Автомобиль {self.name} превышает допустимую скорость!')

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return(f'Автомобиль {self.name} превышает допустимую скорость!')

class SportCar(Car):
    pass

class PoliceCar(Car):
    pass


#Проверка роботоспособности кода
car_1 = TownCar(85, 'Зеленый', 'BMW', False)
car_2 = Car(80, 'Красный', 'Alpha Romeo', False)
car_3 = SportCar(120, 'Желтый', 'Ferrari', False)
car_4 = PoliceCar(75, 'Белый', 'Skoda', True)

print(car_1.go(), car_1.turn('направо'), car_1.show_speed(), car_1.stop(), sep='\n')
print(car_2.show_speed(), car_2.stop(), sep='\n')
print(car_3.turn('налево'), car_3.show_speed(), car_3.police_return(), sep='\n')
print(car_4 .go(), car_4.show_speed(), car_4.police_return(), sep='\n')
