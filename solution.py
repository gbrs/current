from sys import stdin


class Matrix:

    @staticmethod
    def transposed(matrix):
        new_matrix = []
        for j in range(len(matrix.lst[0])):
            inner_list = []
            for i in range(len(matrix.lst)):
                inner_list.append(matrix.lst[i][j])
            new_matrix.append(inner_list)
        return Matrix(new_matrix)

    def __init__(self, lst=[]):
        copy_outer_list = []
        for i in range(len(lst)):
            copy_inner_list = []
            for j in range(len(lst[0])):
                copy_inner_list.append(lst[i][j])
            copy_outer_list.append(copy_inner_list)
        self.lst = copy_outer_list
        # print(lst)

    def __str__(self):
        s = ''
        for i in range(len(self.lst)):
            s = ''.join([s, str(self.lst[i][0])])
            for j in range(1, len(self.lst[0])):
                s = '\t'.join([s, str(self.lst[i][j])])
                # print(i, j, s)
            if i != len(self.lst) - 1:
                s = ''.join([s, '\n'])
        return s

    def size(self):
        return len(self.lst), len(self.lst[0])

    def transpose(self):
        new_matrix = []
        for j in range(len(self.lst[0])):
            inner_list = []
            for i in range(len(self.lst)):
                inner_list.append(self.lst[i][j])
            new_matrix.append(inner_list)
        self.lst = new_matrix
        return self


# exec(stdin.read())

# m = Matrix([[1, 0], [0, 1]])
# print(m)
# m = Matrix([[2, 0, 0], [0, 1, 10000]])
# print(m)
# m = Matrix([[-10, 20, 50, 2443], [-5235, 12, 4324, 4234]])
# print(m)
#
# m1 = Matrix([[1, 0, 0], [1, 1, 1], [0, 0, 0]])
# m2 = Matrix([[1, 0, 0], [1, 1, 1], [0, 0, 0]])
# print(str(m1) == str(m2))
#
# m = Matrix([[1, 1, 1], [0, 100, 10]])
# print(str(m) == '1\t1\t1\n0\t100\t10')
# print(m.size())

# m = Matrix([[1, 2]])
# print(str(m) == '1\t1\t1')
# print(m.size())

# m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
# m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
# print(m1 + m2)
#
# m2 = Matrix([[0, 1, 0], [20, 0, -1]])
# try:
#     m = m1 + m2
#     print('WA\n' + str(m))
# except MatrixError as e:
#     print(e.matrix1)
#     print(e.matrix2)

# m = Matrix([[10, 10], [0, 0], [1, 1]])
# print(m)
# m1 = m.transpose()
# print(m)
# print(m1)

m = Matrix([[10, 10], [0, 0], [1, 1]])
print(m)
print(Matrix.transposed(m))
print(m)
