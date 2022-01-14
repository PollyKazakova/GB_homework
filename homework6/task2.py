'''
Реализовать класс Road (дорога).

определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна;
проверить работу метода.

Например: 20 м*5000 м*25 кг*5 см = 12500 т.
'''



class Road:

    def weigh_asphalt(self, lenght, width):
        self._length = lenght
        self._width = width
        self.weigh = 25
        self.thickness = 5
        weigh_asp = (self._length * self._width * self.weigh * self.thickness) / 1000
        print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна: {weigh_asp:.0f} тонн')


example = Road()
example.weigh_asphalt(20, 5000)
