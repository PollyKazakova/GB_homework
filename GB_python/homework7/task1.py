'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
'''

class Matrix:

    def __init__(self, matrix_data):
        self.matrix_data = matrix_data

    def __str__(self):
        for row in self.matrix_data:
            for i in row:
                print(f'{i:4}', end='')
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.matrix_data)):
            for j in range(len(other.matrix_data[i])):
                self.matrix_data[i][j] = self.matrix_data[i][j] + other.matrix_data[i][j]
        return Matrix.__str__(self)


matrix_data_1 = Matrix([[31, 22, 16], [37, 43, 19], [51, 86, 59]])
matrix_data_2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
print(matrix_data_1 + matrix_data_2)
