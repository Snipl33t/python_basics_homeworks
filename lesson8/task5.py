"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""
from math import sin, cos, sqrt, atan


class ComplexNumber:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return ComplexNumber(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        val = sqrt(self.re**2 + self.im**2) * sqrt(other.re**2 + other.im**2)
        angle = atan(self.im/self.re) + atan(other.im/other.re)
        return ComplexNumber(val * cos(angle), val * sin(angle))

    def __str__(self):
        return f'{round(self.re, 2)} {"+" if self.im > 0 else "-"} {round(abs(self.im), 2)}i'


num1 = ComplexNumber(1, 2)
num2 = ComplexNumber(1, -3)

print(num1)
print(num2)

num3 = num1 + num2

print(num3)

num4 = num1 - num2

print(num4)

num5 = num1 * num2

print(num5)
