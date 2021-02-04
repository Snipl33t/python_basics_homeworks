"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H
+ 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода ткани.

Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


# class Clothing(ABC):
#
#     @abstractmethod


class Clothing(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothing):
    def __init__(self, __size):
        self.__size = __size

    @property
    def fabric_consumption(self):
        return self.__size / 6.5 + 0.5


class Costume(Clothing):
    def __init__(self, __height):
        self.__height = __height

    @property
    def fabric_consumption(self):
        return 2 * self.__height + 0.3


coat1 = Coat(50)
costume1 = Costume(100)

print(f'{coat1.fabric_consumption}')
print(f'{costume1.fabric_consumption}')
