class Matrix():
    def __init__(self, unit_matrix):
        self.unit_matrix = unit_matrix.copy()
        self.ready_matrix = ""
        for element in range(len(self.unit_matrix)):
            for number in range(len(self.unit_matrix[element])):
                self.ready_matrix += f"{self.unit_matrix[element][number]} "
            self.ready_matrix += "\n"
    def __str__(self):
        return self.ready_matrix
    def __add__(self, other):
        between = Matrix(other.unit_matrix) #здесь передаётся ссылка, из-за этого меняется матрица правого операнда, не знаю как это починить
        for element in range(len(other.unit_matrix)):
            for num in range(len(other.unit_matrix[element])):
                between.unit_matrix[element][num] += self.unit_matrix[element][num]
        between.ready_matrix = ""
        for element in range(len(self.unit_matrix)):
            for number in range(len(self.unit_matrix[element])):
                between.ready_matrix += f"{between.unit_matrix[element][number]} "
            between.ready_matrix += "\n"
        return between.ready_matrix
matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_sec = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(matrix)
print(matrix_sec)
print(matrix + matrix_sec)
print(matrix + matrix_sec)