"""
Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
округление значения до целого числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод
позволяет организовать ячейки по рядам.

Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n**.

Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n*****.
"""
from math import floor


class Cell:
    def __init__(self, number_of_cells):
        self.number_of_cells = number_of_cells

    def __add__(self, other):
        return Cell(self.number_of_cells + other.number_of_cells)

    def __sub__(self, other):
        if self.number_of_cells is not other.number_of_cells:
            return Cell(abs(self.number_of_cells - other.number_of_cells))
        TypeError('Cells cannot be the same!')

    def __mul__(self, other):
        return Cell(self.number_of_cells * other.number_of_cells)

    def __truediv__(self, other):
        if self.number_of_cells > other.number_of_cells:
            return Cell(self.number_of_cells // other.number_of_cells)
        else:
            return Cell(other.number_of_cells // self.number_of_cells)

    def make_order(self, row_size):
        number_of_rows = self.number_of_cells / row_size
        temp_str = ''
        for rows in range(0, floor(number_of_rows)):
            temp_str += '#' * row_size + '\n'
        if number_of_rows % 1:
            temp_str += '#' * (self.number_of_cells - row_size * floor(number_of_rows)) + '\n'
        return temp_str


cell1 = Cell(12)
cell2 = Cell(14)

print(f'Cell1 has {cell1.number_of_cells} cells, Cell2 has {cell1.number_of_cells} cells')

cell3 = cell1 + cell2
print(f'Cell1 + Cell2 create a cell with {cell3.number_of_cells} number of cells')

cell4 = cell2 - cell1
print(f'Cell1 - Cell2 create a cell with {cell4.number_of_cells} number of cells')

cell5 = cell1 * cell2
print(f'Cell1 * Cell2 create a cell with {cell5.number_of_cells} number of cells')

cell6 = cell1 / cell2
print(f'Cell1 / Cell2 create a cell with {cell6.number_of_cells} number of cells')

print(cell3.make_order(5))
