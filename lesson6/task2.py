"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса
асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу
метода.
"""


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self, mass_per_cm, asphalt_width):
        return self._length * self._width * mass_per_cm * asphalt_width


road = Road(20, 5000)

print(f'Mass of the asphalt for given parameters is {road.asphalt_mass(25, 5) // 1000} tons')
