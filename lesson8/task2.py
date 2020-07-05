"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivisionErr(Exception):
    def __init__(self, txt):
        self.txt = txt


a = int(input('Type dividend: '))
b = int(input('Type divisor: '))

try:
    if b == 0:
        result = '-'
        raise MyZeroDivisionErr('User divided by zero!!! Assuming it is an infinitely small value')
    else:
        result = a / b
except MyZeroDivisionErr as e:
    print(e)
    result = float('inf')
finally:
    print(f'{a} / {b} = {result}')
