"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date: str):
        self.date = date

    @classmethod
    def get_date(cls, func_str):
        try:
            date_list = list(map(int, func_str.split('-')))
            Date.validate_date(date_list)
            return date_list
        except ValueError as e:
            print("Enter a correct date!")
            print(e)

    @staticmethod
    def validate_date(date):
        for itm in date:
            if itm < 1:
                raise ValueError("Dates can't be negative!")
        if date[0] > 31 or date[1] > 12:
            raise ValueError("Check your day or/and month!")


print(Date.get_date('24-11-1997'))

