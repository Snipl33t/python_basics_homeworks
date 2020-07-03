"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух
матриц). Результатом сложения должна быть новая матрица.
"""


class Matrix:
    def __init__(self, data: list):
        self.data = data

    def __str__(self):
        temp_str = '\n'
        for row in self.data:
            temp_str += '\t'.join([str(itm) for itm in row]) + '\n'
        return temp_str

    def __add__(self, other):
        if (len(self.data) is len(other.data)) and (len(self.data[0]) is len(other.data[0])):
            # First connect the two matrices together in tuples
            output_data = [list(zip(self.data[idx], other.data[idx])) for idx, itm in enumerate(self.data)]
            # Then sum each tuple
            output_data = [list(map(sum, row)) for row in output_data]
            return Matrix(output_data)
        TypeError('Matrices should be of the same length!')


matrix_a = [[1, 2, 3],
            [5, 8, 1],
            [12, 3, 2]]

matrix_b = [[5, 21, 4],
            [6, 2, 43],
            [11, 12, 8]]

mat_a = Matrix(matrix_a)
mat_b = Matrix(matrix_b)

print(f'Matrix A: {mat_a}')
print(f'Matrix B: {mat_b}')

mat_c = mat_a + mat_b

print(f'Matrix C: {mat_c}')
