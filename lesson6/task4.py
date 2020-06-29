"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат.
"""
from random import choice


class Car:
    def __init__(self, name, color, max_speed, is_police=False):
        self.name = name
        self.color = color
        self.max_speed = max_speed
        self.is_police = is_police
        self.speed = 0

    def go(self, acceleration):
        if self.speed + acceleration > self.max_speed:
            print(f"{self.name} can't drive faster than {self.max_speed}")
        self.speed += acceleration

    def stop(self):
        self.speed = 0
        print(f'{self.name} has stopped')

    def turn(self, direction):
        print(f'{self.name} has turned to the {direction}')

    def show_speed(self):
        print(f"{self.name}'s speed = {self.speed}")


class TownCar(Car):
    def __init__(self, name, color, max_speed):
        super().__init__(name, color, max_speed)

    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name} exceeded speed limit! Speed = {self.speed} and the speed limit is 60!")
        else:
            print(f"{self.name}'s speed = {self.speed}")


class WorkCar(Car):
    def __init__(self, name, color, max_speed):
        super().__init__(name, color, max_speed)

    def show_speed(self):
        if self.speed > 40:
            print(f"{self.name} exceeded speed limit! Speed = {self.speed} and the speed limit is 40!")
        else:
            print(f"{self.name}'s speed = {self.speed}")


class SportCar(Car):
    def __init__(self, name, color, max_speed):
        super().__init__(name, color, max_speed)


class PoliceCar(Car):
    def __init__(self, name, color, max_speed, is_police):
        super().__init__(name, color, max_speed, is_police)


car1 = TownCar('Volga', 'silver', 130)
print(f"Car - {car1.name}, color - {car1.color}, maximum speed - {car1.max_speed}, police car - {car1.is_police}")
car1.go(50)
car1.show_speed()
car1.turn(choice(['left', 'right']))
car1.go(20)
car1.show_speed()
car1.stop()
print('\n')

car2 = WorkCar('Nissan', 'blue', 170)
print(f"Car - {car2.name}, color - {car2.color}, maximum speed - {car2.max_speed}, police car - {car2.is_police}")
car2.go(50)
car2.show_speed()
car2.turn(choice(['left', 'right']))
car2.go(20)
car2.show_speed()
car2.stop()
print('\n')

car3 = SportCar('Porsche', 'red', 220)
print(f"Car - {car3.name}, color - {car3.color}, maximum speed - {car3.max_speed}, police car - {car3.is_police}")
car3.go(100)
car3.show_speed()
car3.turn(choice(['left', 'right']))
car3.go(60)
car3.show_speed()
car3.stop()
print('\n')

car4 = PoliceCar('Lada', 'silver', 200, True)
print(f"Car - {car4.name}, color - {car4.color}, maximum speed - {car4.max_speed}, police car - {car4.is_police}")
car4.go(50)
car4.show_speed()
car4.turn(choice(['left', 'right']))
car4.go(40)
car4.show_speed()
car4.stop()
