"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
from time import sleep


class TrafficLights:
    _color = [['red', 3.5], ['yellow', 1], ['green', 3.5], ['yellow', 1]]

    def running(self):
        for segment in self._color:
            # print(segment[0])
            # sleep(segment[1])
            yield print(segment[0])
            yield sleep(segment[1])


traffic_lights1 = TrafficLights()
traffic_lights2 = TrafficLights()
var1 = traffic_lights1.running()
var2 = traffic_lights2.running()

try:
    while True:
        next(var1)
        next(var2)
except StopIteration:
    pass
