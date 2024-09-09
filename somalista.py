import math
import numpy as np

def insertnumb():
    i = int(input("Digite o tamanho da lista: "))
    for j in range(i):
        n = int(input("Digite os números da lista: "))
        ln.append(n)
    print("A lista foi formada")

def addlist():
    print(f'A soma dos números da lista é: {sum(ln)}')

def factorialista():
    for num in ln:
        n = math.factorial(num)
        fl.append(n)
    print(f'O fatorial dos números da lista são: {fl}')

def tam_matriz(matriz_n):
    lin = int(input("Digite o número de linhas da matriz {matriz_n}: "))
    col = int(input("Digite o número de colunas da matriz {matriz_n}: "))
    return lin, col

def insertmatriz(lin,col,matriz_n):
    print(f'\nDigite os elementos da matriz {matriz_n} ({lin} x {col}): ')
    matriz = []
    for i in range(lin):
        lin = []
        for j in range(col):
            e = int(input(f'Elemento ({i+1}, {j+1}): '))
            lin.append(e)
        matriz.append(lin)
    return np.array(matriz)

def mult_matrizes():
    print(f'Matriz A: \n{A}')
    print(f'Matriz B: \n{B}')
    print(f'Resultado: \n{C}')

if __name__ == '__main__':
    ln = []
    fl = []
    lin_A, col_A = tam_matriz("A")
    lin_B,col_B = tam_matriz("B")
    if col_A != lin_B:
        print("O número de colunas da matriz A deve ser igual ao número de linhas da matriz B")
    else:
        A = insertmatriz(lin_A, col_A, "A")
        B = insertmatriz(lin_B, col_B, "B")
        C = np.dot(A,B)
    tam_matriz()
    insertmatriz()
    mult_matrizes()
