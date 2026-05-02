import numpy as np

'''x=np.zeros((2,3))
print(x)'''

'''y=np.ones((3,2))
print(y)'''

'''z=np.eye((3))
print(z)'''

'''matriz=[
    [1,2,3],
    [4,5,6]
]

elemento=matriz[1][2]
print('Elemento',elemento)

matriz[0][1]=9
print('matriz modificada:',matriz)'''

'''arr_float=np.array([1,2,3],dtype=float)
arr_tuple=np.array((4,5,6))
print(arr_float)
print(arr_tuple)'''

'''A=np.array([[1, 2, 3], [4, 5]])
np.sum(A)
print(A)'''

'''A=np.array([[1,2],[3,4]])
np.mean(A)
print(A)'''

'''A=np.array([[1,2],[3,4]])
np.max(A)
print(A)'''

'''A=np.array([[1,2],[3,4]])
np.min(A)
print(A)'''

#lista de exercicios

#exer 1
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
soma = 0
for linha in matriz:
    for item in linha:
        soma += item
print(soma)

#exerc 2
n = int(input("Ordem da matriz: "))
matriz = []
for i in range(n):
    linha = []
    for j in range(n):
        linha.append(1 if i == j else 0)
    matriz.append(linha)
for linha in matriz:
    print(linha)

#exerc 3
matriz = [[10, 20, 30, 40], [50, 60, 70, 80], [15, 25, 35, 45], [55, 65, 75, 85]]
alvo = int(input("Digite um número: "))
encontrado = False
for linha in matriz:
    if alvo in linha:
        encontrado = True
        break
print("Está na matriz" if encontrado else "Não está na matriz")

#exerc 4
matriz = [[1, 2], [3, 4]]
matriz[0], matriz[1] = matriz[1], matriz[0]
print(matriz)

#exerc 5
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
escalar = float(input("Número real: "))
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] *= escalar
for linha in matriz:
    print(linha)

#exerc 6
matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
pares = 0
for linha in matriz:
    for item in linha:
        if item % 2 == 0:
            pares += 1
print(pares)

#exerc 7
import random
matriz = [[random.randint(1, 100) for _ in range(3)] for _ in range(3)]
maior = matriz[0][0]
for linha in matriz:
    for item in linha:
        if item > maior:
            maior = item
print(matriz)
print(maior)

#exerc 8
matriz = [[10, 20, 30], [5, 15, 25], [100, 200, 300]]
for linha in matriz:
    media = sum(linha) / len(linha)
    print(media)

#exerc 9
matriz = [[1]*4, [2]*4, [3]*4, [4]*4]
soma = 0
for i in range(4):
    soma += matriz[i][i]
print(soma)

#exerc 10
m, n = 3, 2
matriz = [[1, 2], [3, 4], [5, 6]]
transposta = []
for j in range(n):
    linha = []
    for i in range(m):
        linha.append(matriz[i][j])
    transposta.append(linha)
print(transposta)

#exerc 11
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
somas = [0, 0, 0]
for j in range(3):
    for i in range(3):
        somas[j] += matriz[i][j]
print(somas)

#exerc 12
matriz = [[1, 2, 3], [2, 5, 4], [3, 4, 6]]
simetrica = True
n = len(matriz)
for i in range(n):
    for j in range(n):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False
            break
print(simetrica)

#exerc 13
matriz = [[(i+j) for j in range(5)] for i in range(5)]
n = 5
secundaria = []
for i in range(n):
    secundaria.append(matriz[i][n - 1 - i])
print(secundaria)

#exerc 14
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        for k in range(2):
            C[i][j] += A[i][k] * B[k][j]
print(C)

#exerc 15
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(matriz)
for i in range(n // 2):
    for j in range(i, n - i - 1):
        temp = matriz[i][j]
        matriz[i][j] = matriz[n - 1 - j][i]
        matriz[n - 1 - j][i] = matriz[n - 1 - i][n - 1 - j]
        matriz[n - 1 - i][n - 1 - j] = matriz[j][n - 1 - i]
        matriz[j][n - 1 - i] = temp
for linha in matriz:
    print(linha)


















