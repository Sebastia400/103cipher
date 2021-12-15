##
## EPITECH PROJECT, 2021
## 103cipher
## File description:
## main.py
##
from multiplication import *
import sys
def printmatrix(matrix):
    for i in range (len(matrix)):
        for j in range (len(matrix)):
            print(matrix[i][j], end = " ")

def encrypt_decrypt(argv):
    
    if (argv[3] == '1'):
        print("DESENCRIPTATGE:")

    elif (argv[3] == '0'):
        n, matrix_key = key_matrix(sys.argv[2])
        matrix = sentence_to_ascii(n, sys.argv[1])
        encriptedmesage = multiplication(matrix_key,matrix,n)
        print("Encrypted message:")
        printmatrix(encriptedmesage)

def size_array(word):
    length = len(word)
    arraymatrix = [0,1,2,3,4,5,6,7,8,9,10]
    for i in arraymatrix:
        valuematrix = i * i
        if (length <= valuematrix):
            return i
    sys.exit(84)

def print_key (key_matrix): ## Impresió de la clau de encriptament
    print("Key matrix:")
    for i in range (len(key_matrix)):
        for j in range (len(key_matrix[i])): ## ara hem de encriptar la frase vale, que bueno ja tenim la funcio, no? a si? multiplicacion?
            print(key_matrix[i][j], end = '\t')
        print('') 
    print()
def sentence_to_ascii(lenmatrix, sentence): 
    
    sentence_ascii = []
    word = []
    j = 0
    k = 0
    
    for i in range (len(sentence)):
        if (lenmatrix > j):
            word.append(ord(sentence[i]))
            j += 1
        if (j == lenmatrix):
            sentence_ascii.append(word)
            j = 0
            word = []
    
    while ((len(word) < lenmatrix) and (len(word) > 0)):
        word.append(0)
    if(len(word) != 0):
        sentence_ascii.append(word)
    
    return (sentence_ascii)

def key_matrix(word): ## generació de la clau de encriptació
    n = size_array(word)
    x = []
    y = []
    k = 0
    i = 0
    j = 0
    
    for j in range(n):
        y = []
        for i in range(n):
            if (k < len(word)):
                y.append(ord(word[k]))
            else:
                y.append(0)
            k += 1
        x.append(y)
    print_key (x)
    return (n, x)
def errormanage(argv):
    if(len(argv) != 4):
        print("ERROR (falten o sobren arguments)")
        sys.exit(84)
    if(int(argv[3]) < 0 or int(argv[3]) > 1):
        print("ERROR (ultim valor erroni)")
        sys.exit(84)
    ##if (len(argv[3]) % 13 or len(argv[3]) % 2 or len(argv[3]) == 0):
    ##    print("ERROR (determinat of encryption)")



def main():
    errormanage(sys.argv)
    ##n, matrix_key = key_matrix(sys.argv[2])
    ##matrix = sentence_to_ascii(n, sys.argv[1])
    ##encriptedmesage = multiplication(matrix_key,matrix,n)
    encrypt_decrypt(sys.argv)
    

##matrix1 = [[7,4,1], [7,4,1], [7,4,1]]
#print("det:")
#print(det(matrix1))
##print("mod:")## res jaajajjajaaj xd vaig a fer la inversa
##print(mod(matrix1)) 

##matrix2 = [[7],[4]]
##matriu encriptar
##matriu_encript = [[6,24,1],[13,16,10],[20,17,15]]
##getMatrixInverse(matriu_encript)
##print(inverse_matrix(matriu_encript))

##multiplication(matriu_encript,matrix1)
##funcio main
##multiplication(matrix1, matrix2)
main()
