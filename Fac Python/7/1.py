class Matrix:
    def __init__(self, m):
        self.matrix = m

    def __str__(self):
        return '\n'.join(' '.join([str(elem) for elem in st]) for st in self.matrix)

    def __add__(self, other):
        return Matrix(list(map(sum, zip(self.matrix[i]), (other.matrix[i]))) for i in range(len(self.matrix)))


m1 = Matrix([[1, 2, 3], [4, 5, 6]])
print(m1)
m2 = Matrix([[7, 8, 9], [10, 11, 12]])
print(m2)
print(m1+m2)

