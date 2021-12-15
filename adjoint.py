def modified_matrix(row, colum, matrix):
    x = []
    j = 0
    i = 0
    while j < len(matrix):
        i = 0
        if j == row:
            j += 1
        y = []
        while i < len(matrix[j]):
            if i == colum:
                i += 1
            y.append(matrix[j][i])
            i += 1
        x.append(y)
        j += 1
    return x

def adjoint(matrix):
    result = 0
    x = []
    for j in range(len(matrix) - 1):
        y = []
        for i in range(len(matrix[j]) - 1):
            matrix_mod = modified_matrix(j, i, matrix)
            result = -1 ** (j + i)*(matrix_mod[j][i] * matrix_mod[j][i + 1] - matrix_mod[j + 1][i] * matrix_mod[j + 1][i + 1])
            print(result)
            y.append(result)
        x.append(y)
    return x

matrix = [[1,2,6,-1], [0, 2, 1, -4], [-1, 3, 2, 1], [4, 1, 0, -1]]
print(modified_matrix(0, 0, matrix))
print(adjoint(matrix))