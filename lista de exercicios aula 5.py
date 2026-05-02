'''aluno1=input('digite o nome do aluno1:')
aluno2=input('digite o nome do aluno2:')
aluno3=input('digite o nome do aluno3:')
print('os alunos da turma são: \n %S \n %S \n %S' % (aluno1,aluno2.aluno3))'''

'''nomes_alunos = []
for i in range (3):
    nome=input(f'digite o nome dos alunos {i+1}:')
    nomes_alunos.append(nome)
print('\nNome dos alunos registrados')
for nome in nomes_alunos:
    print(nome)'''

#exerc 1
'''a=[]
for i in range(10):
num=int(input('digite um numero:'))
i+=1
a. append(num)'''
#exerc 2
'''a=[]
for i in range(10):
num=int(input('digite um numero:'))
i+=1
a. append(num)
print('\n os numeros sao:')
for num in a
print(num)'''
#exerc 3
'''a=[]
for i in range(10):
num=int(input('digite um numero:'))
i+=1
a. append(num)
menor_valor=min(a)
maior_valor=max(a)
print('menor_valor')
print('maior valor')'''
#exerc 4
'''lista=[]
quant=int(input('digite o numero de alunos:'))
for i in range(quant)
nota=int(input(f'digite a nota do aluno {i=1}:'))
lista.append(nota)
abaixo=0
acima=0
for nota in lista
if nota<60
abaixo+=1
else
acima+=1
print(f'alunos abaixo da media: {abaixo}')
print(f'alunos acima da media: {acima}')'''
#exerc 5
'''a=[]
for i in range(5):
num=int(input('digite um numero:'))
i+=1
a.append(num)
menor_valor=min(a)
maior_valor=max(a)
total=sum(num)
media = sum(a) / len(a)'''

#lista de exercicios

#exerc 1
lista= [1,2,3,4,5]

print(lista)

#exerc 2
lista_cores = ['vermelho', 'azul', 'verde', 'amarelo']

print(lista_cores[1])

#exerc 3
lista = [1,2,3]

lista.append(10)

print(lista)

#exerc 4
lista_frutas = ['maça', 'banana', 'laranja']

lista_frutas.remove("banana")

print(lista_frutas)

#exerc 5
lista = [10,20,30,40,50]

tamanho = len(lista)

print(tamanho)

#exerc 6
lista = [1,2,3,4,5,6,7]

verificacao =  7 in lista
print(verificacao)

#exerc 7
lista = [1,2]
lista2 = [3,4]

lista3= lista + lista2

print(lista3)

#exerc 8
lista_letras= ['a', 'b', 'c', 'd']

lista_inversa = lista_letras[::-1]

#exerc 9
lista=[1,2,3,2,3,2,2,5]

quantidade = lista.count(2)

print(quantidade)

#exerc 10
lista = [10.5, 20, 15.5]

soma = sum(lista)

print(soma)

#exerc 11
lista1 = [1,2,3,4,5,6]
lista2 = [4,5,6,7,8,9]

res = list(dict.fromkeys(lista1+lista2))

print(res)

#exerc 12
lista = [10, 20, 150, 30, 40]

lista.sort()

menor = lista[0]

maior = lista[-1]

print(f"o maior: {maior}, e o menor: {menor}")

#exerc 13
lista = [i**2 for i in range (1,11)]
print(lista)

#exerc 14
lista = [1,2,3,4,6,7,8,9,45,46,67,89]

lista_impares = [x for x in lista if x % 2 !=0]

print(lista_impares)

#exerc 15
lista = [1, 2, 3, 4, 5]
n = 2

lista_rotacionada = lista[-n:] + lista[:-n]

print(lista_rotacionada)

#exerc 16
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

intersecao = [item for item in lista1 if item in lista2]

print(intersecao)

#exerc 17
matriz = [[1,2],[3,4]]
achatada= [item for sublista in matriz for item in sublista]
print(achatada)

#exerc 18
lista = [38, 27, 43, 3, 9, 82, 10]
n = len(lista)
tamanho_bloco = 1

while tamanho_bloco < n:
    for i in range(0, n, 2 * tamanho_bloco):
        meio = min(i + tamanho_bloco, n)
        fim = min(i + 2 * tamanho_bloco, n)

        esquerda = lista[i:meio]
        direita = lista[meio:fim]

        p_esq = 0
        p_dir = 0
        p_lista = i

        while p_esq < len(esquerda) and p_dir < len(direita):
            if esquerda[p_esq] < direita[p_dir]:
                lista[p_lista] = esquerda[p_esq]
                p_esq += 1
            else:
                lista[p_lista] = direita[p_dir]
                p_dir += 1
            p_lista += 1

        while p_esq < len(esquerda):
            lista[p_lista] = esquerda[p_esq]
            p_esq += 1
            p_lista += 1

        while p_dir < len(direita):
            lista[p_lista] = direita[p_dir]
            p_dir += 1
            p_lista += 1

    tamanho_bloco *= 2

print(lista)

#exerc 19
numeros = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_atual = max_global = numeros[0]

for i in range(1, len(numeros)):
    max_atual = max(numeros[i], max_atual + numeros[i])
    if max_atual > max_global:
        max_global = max_atual

print(max_global)

#exerc 20
nums = [1, 2, 3]
permutações = [[]]

for n in nums:
    novas_permutações = []
    for p in permutações:
        for i in range(len(p) + 1):
            nova_p = p[:i] + [n] + p[i:]
            novas_permutações.append(nova_p)
    permutações = novas_permutações

print(permutações)