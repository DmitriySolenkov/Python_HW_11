from random import randint


class Matrix():
    ### Documentation ###

    def __init__(self, lines, rows):
        self.rows = rows
        self.lines = lines
        self.sum = 0
        self.matrix = []
        for i in range(lines):
            self.matrix.append([0]*rows)

    def matrix_fill(self):
        ### Def to fill matrix with random numbers ###
        for i in range(self.lines):
            for j in range(self.rows):
                self.matrix[i][j] = randint(1, 10)
                self.sum += self.matrix[i][j]

    def __str__(self):
        string = ""
        for i in range(len(self.matrix)):
            string += "\n["
            for j in range(len(self.matrix[0])):
                string += " " + str(self.matrix[i][j])
            string += " ]"
        return string

    def __add__(self, other):
        ### Def to sum two matrixes ###
        lines = min(self.lines, other.lines)
        rows = min(self.rows, other.rows)
        matrix_sum = Matrix(rows, lines)
        for i in range(lines):
            for j in range(rows):
                matrix_sum.matrix[i][j] = self.matrix[i][j] + \
                    other.matrix[i][j]
        return matrix_sum

    def matrix_transpos(self):
        new_matrix = Matrix(self.rows, self.lines)
        for i in range(self.lines):
            for j in range(self.rows):
                new_matrix.matrix[i][j] = self.matrix[j][i]
        return new_matrix

    def __eq__(self, other):
        return (self.sum == other.sum)

    def __ne__(self, other):
        return (self.sum != other.sum)

    def __gt__(self, other):
        return (self.sum > other.sum)

    def __ge__(self, other):
        return (self.sum >= other.sum)

    def __lt__(self, other):
        return (self.sum < other.sum)

    def __le__(self, other):
        return (self.sum <= other.sum)

    def __doc__(self):
        print("rgregergrgrg")


matrix1 = Matrix(3, 3)
matrix1.matrix_fill()
print(matrix1)
print(f"{matrix1.sum = }")
matrix2 = Matrix(3, 3)
matrix2.matrix_fill()
print(matrix2)
print(f"{matrix2.sum = }")
matrix_sum = matrix1+matrix2
print(matrix_sum)

print(matrix1 == matrix2)
print(matrix1 != matrix2)
print(matrix1 > matrix2)
print(matrix1 >= matrix2)
print(matrix1 < matrix2)
print(matrix1 <= matrix2)


print(matrix_sum.matrix_transpos())

help(Matrix)
help(Matrix.matrix_fill)
