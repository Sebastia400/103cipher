##
## EPITECH PROJECT, 2021
## 103cipher
## File description:
## multiplication.py
##
import sys
from copy import deepcopy
"""
def multiplication(matrix1, matrix2):
    n = size_array(word)
    x = []
    y = []
    k = 0
    i = 0
    j = 0
    
    print (n)
    for j in range(len(matrix1)):
        y = []
        for i in range(len(matrix2)):
                y.append(0)
        x.append(y)
    result = [[0],[0]] 
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
                
    print(result)
"""
    
def multiplication(matrix_encript, matrix1, lenmatrix): ## matrix 1 seran les lletres que hem guardat
    matrix_final = []
    x = []
    resultat = 0
    for i in range(len(matrix1)):
        x = []
        for j in range(len(matrix_encript)): ## recorrem la longitud la matriu a encriptar
            resultat = 0
            for k in range(lenmatrix):
                resultat += matrix_encript[k][j] * matrix1[i][k]
            x.append(resultat)
        matrix_final.append(x)
    return (matrix_final)

def mod(matrix):
    for j in range(len(matrix)):
        for i in range(len(matrix[j])):
            matrix[j][i] = matrix[j][i] % 26
    return matrix

def small_matrix(matrix, row, colum): 
    new_matrix = deepcopy(matrix)
    new_matrix.remove(matrix[row])
    for i in range(len(new_matrix)):
        new_matrix[i].remove(new_matrix[i][colum])
    return new_matrix 

def det(matrix):
    nbr_rows = len(matrix)
    for row in matrix:
        if len(row) != nbr_rows: 
            return 84
    if len(matrix) == 2:
        s_det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return s_det
    else:
        result = 0
        nbr_cols = nbr_rows 
        for j in range(nbr_cols):
            cofactor = (-1) ** j * matrix[0][j] * det(small_matrix(matrix, 0, j))
            result += cofactor
        return result
"""
def zero_matrix(matrix):
    A = []
    for i in range(rows, cols):
        A.append([])
        for i in range(rows):
            A[-1].append(0.0)
        return A
"""
def zeros_matrix(rows, cols):
    A = []
    for i in range(rows):
        A.append([])
        for j in range(cols):
            A[-1].append(0.0)

    return A

def copy_matrix(M):
    rows = len(M)
    cols = len(M[0])

    MC = zeros_matrix(rows, cols)

    for i in range(rows):
        for j in range(rows):
            MC[i][j] = M[i][j]

    return MC

def identity(matrix):
    x = []
    k = 0
    for j in range(len(matrix)):
        y = []
        for i in range(len(matrix)):
            if i == k:
                y.append(1)
            else:
                y.append(0)
        k += 1
        x.append(y)
    return x


def inverse_matrix(matrix):
    if det(matrix) != 0:
        a_copy = copy_matrix(matrix)
        identity_matrix = identity(matrix)
        print(identity_matrix)
        i_copy = copy_matrix(identity_matrix)

        indices = list(range(len(matrix)))

        for fd in range(len(matrix)):
            fd_scaler = 1.0 / a_copy[fd][fd]
            for j in range(len(matrix)):
                a_copy[fd][j] *= fd_scaler
                i_copy[fd][j] *= fd_scaler
            for i in indices[0:fd] + indices[fd+1:]:
                cr_scaler = a_copy[i][fd]
                for j in range(len(matrix)):
                    a_copy[i][j] *= a_copy[i][j] - cr_scaler * a_copy[fd][j]
                    i_copy[i][j] *= i_copy[i][j] - cr_scaler * i_copy[fd][j]
        return i_copy
    else:
        print("Can't be inverted")
        sys.exit (84)
