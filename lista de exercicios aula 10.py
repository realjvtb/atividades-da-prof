#exerc 1
'''def metros_para_centimetros(metros):
    return metros * 100

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32'''

#exerc 2

'''nome_grande = texto.transformar_em_maiusculo(nome)
print("nome original:", nome, "| nome modificado:", nome_grande)

frase_mista = "programa em python"
frase_pequena = texto.transformar_em_minusculo(frase_mista)
print("texto original:", frase_mista, "| em minusculo:", frase_pequena)'''

#exerc 3
'''import conversor
import texto

print("--- testes do conversor ---")

metros = 5
cm = conversor.metros_para_centimetros(metros)
print(metros, "metros sao", cm, "centimetros")

temperatura = 0
f = conversor.celsius_para_fahrenheit(temperatura)
print(temperatura, "graus celsius equivalem a", f, "graus fahrenheit")

print("\n--- testes de texto ---")

palavra = "teclado"
tamanho = texto.contar_letras(palavra)
print("A palavra", palavra, "tem", tamanho, "letras")

nome = "felipe"

#exerc 2
'
nome_grande = texto.transformar_em_maiusculo(nome)
print("nome original:", nome, "| nome modificado:", nome_grande)

frase_mista = "programa em python"
frase_pequena = texto.transformar_em_minusculo(frase_mista)
print("texto original:", frase_mista, "| em minusculo:", frase_pequena)'''

#exer 4
'''def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "erro: divisao por zero"
    return a / b'''

#exer 5
'''def cadastrar_nome():
    nome = input("digite seu nome: ")
    return nome

def boas_vindas(nome):
    print("seja bem-vindo,", nome)
    
#segunda parte
import usuario
import operacoes

nome_usuario = usuario.cadastrar_nome()
usuario.boas_vindas(nome_usuario)

print("\n--- testando as operacoes ---")

n1 = 10
n2 = 2

resultado_soma = operacoes.soma(n1, n2)
print("soma:", resultado_soma)

resultado_sub = operacoes.subtracao(n1, n2)
print("subtracao:", resultado_sub)

resultado_mult = operacoes.multiplicacao(n1, n2)
print("multiplicacao:", resultado_mult)

resultado_div = operacoes.divisao(n1, n2)
print("divisao:", resultado_div)'''

#exerc 6
'''import math

def area_quadrado(lado):
    return lado * lado

def area_circulo(raio):
    return math.pi * (raio ** 2)

def perimetro_retangulo(base, altura):
    return 2 * (base + altura)'''