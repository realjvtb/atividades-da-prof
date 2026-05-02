#exerc 1
'''idade=int(input('digite sua idade:'))
if idade >= 16:
    print('voce ja pode votar')
else:
    print('voce ainda não pode votar')'''
from selectors import SelectSelector

#exerc 2
'''numero=int(input('digite um numero:'))
if numero > 0:
    print(f'o numero {numero} e positivo.')
elif numero < 0:
    print(f'o numero {numero} e negativo.')
else:
    print('o numero e 0')'''

#exerc 3
'''valor = float(input("Digite o valor total da compra: R$ "))
if valor > 100:
    desconto = valor * 0.10
    valor_final = valor - desconto
    print(f"Você ganhou 10% de desconto!")
    print(f"Valor final a pagar: R$ {valor_final:.2f}")
else:
    print(f"Valor da compra: R$ {valor:.2f}")
    print("Nas compras acima de R$ 100, você ganha 10% de desconto!")'''

#exerc 4
'''nota=float(input('digite sua nota:'))
if nota > 9.0:
    print('parabens voce foi aprovado')
elif nota > 7.0:
    print('voce esta aprovado')
elif 4.0 <= nota <= 6.9:
    print('voce esta em recuperação')
else: nota < 4.0:
    print('voce esta reprovado')'''

#exerc 5
'''numero=int(input('digite um numero'))
if numero = % ==2
    print(f'o numero {numero} e par')
else
print(f'o numero {numero} e impar')'''

#exerc 6
'''n1=int(input('digite um numero:'))
n2=int(input('digite um numero:'))
if n1>n2:
    print(f'o numero {n1} e maior que {n2}')
else:n1<n2
print(f'o numero {n1} e menor que {n2}')'''

#exerc 7
'''usuario_correct:= admin
nome=int(input('digite o nome do usuario'))
if nome = admin
    print('acesso liberado:')
else:
print('usuario desconhecido')'''

#exerc 8
'''peso=float(input('digite se peso:'))
altura=float(input('digite sua altura:'))
imc=peso/(altura**2)
if imc > 25:
    print('acima do peso ideal')
else:
    print('peso dentro da atualidade')'''

#exerc 9
'''n1=float(input('digite quantos cm tem um lado do triangulo:'))
n2=float(input('digite quantos cm tem um lado do triangulo:'))
n3=float(input('digite quantos cm tem um lado do triangulo:'))
if n1==n2==n3:
    print('o triangulo é equilatero')
elif n1 == n2 or n1 == n3 or n2 == n3:
    print('o triangulo é isócesles')
else:
    print('o triangulo é equilatero')'''

#exerc 10
'''n1=int(input('informe um numero:'))
if n1%5==0:
    print(f'o numero {n1} e multiplo de 5')
else:
    print(f'o numero {n1} nao e multiplo de 5')'''

#exerc 11
'''n1=int(input('digite sua idade:'))
if n1==5 <= n1 <=7:
    print('infantil A')
elif n1==8 <= n1 <= 10:
    print('infantil B')
elif n1==11 <= n1 <= 13:
    print('juvenil A')
elif n1==14 <= n1 <= 17:
    print('juvenil B')
else:n1>=18
print('adulto')'''

#exerc 12
'''distancia = float(input("qual a distância que você deseja percorrer:"))

if distancia <= 200:
    preco por km = 0.50
else:
    preco por km = 0.45

total = distancia * preco por km

print(f"para uma viagem de {distancia}km,o preço da passagem será R$ {total:.2f}")'''

#exerc 13

'''ano=int(input('informe um ano:'))
if ano%4==0:
    print(f'o ano {ano} e bisexto')
else:
    print(f'o ano {ano} nao e bisexto')'''

#exerc 14

'''salario = float(input("Digite o salário do funcionário: R$ "))

if salario > 1621.00:
    aumento = salario * 0.10
    novo_salario = salario + aumento
    percentual = "10%"
else:
    aumento = salario * 0.15
    novo_salario = salario + aumento
    percentual = "15%"

print(f"O aumento será de {percentual} (R$ {aumento:.2f}).")
print(f"O novo salário é: R$ {novo_salario:.2f}")'''

#exerc 15

'''velocidade = float(input("Qual é a velocidade do carro (km/h)? "))
if velocidade > 80:
    print("\nVocê foi MULTADO! O limite é 80 km/h.")
    km_acima = velocidade - 80
    valor_multa = km_acima * 7.00
    print(f"Você excedeu o limite em {km_acima:.1f} km/h.")
    print(f"O valor da multa é: R$ {valor_multa:.2f}")
else:
    print("\nVelocidade dentro do limite permitido. Tenha uma boa viagem!")'''

#exerc 16

'''celsius = float(input("Digite a temperatura em Celsius: "))
opcao = input("Deseja converter para Fahrenheit (F) ou Kelvin (K)? ").upper()

if opcao == 'F':
    resultado = (celsius * 9/5) + 32
    print(f"{celsius}°C é igual a {resultado:.2f}°F")
elif opcao == 'K':
    resultado = celsius + 273.15
    print(f"{celsius}°C é igual a {resultado:.2f}K")
else:
    print("Opção inválida. Escolha F ou K.")'''

#exerc 17

'''area = float(input("Qual o tamanho da área a ser pintada (m²)? "))

litros_necessarios = area / 3
latas_necessarias = litros_necessarios / 18

print(f"Você precisará de {litros_necessarios:.2f} litros de tinta.")

if latas_necessarias <= 1:
    print("Você precisa de apenas 1 lata. Custo: R$ 80,00")
else:
    total_latas = int(latas_necessarias) + (1 if latas_necessarias % 1 > 0 else 0)
    custo_total = total_latas * 80
    print(f"Você precisará de {total_latas} latas. Custo total: R$ {custo_total:.2f}")'''

#exerc 18

'''valor_casa = float(input("Valor da casa: "))
salario = float(input("Salário do comprador: "))
anos = int(input("Anos para pagar: "))

prestacao = valor_casa / (anos * 12)
limite = salario * 0.30

if prestacao <= limite:
    print(f"Empréstimo aprovado! Prestação: R$ {prestacao:.2f}")
else:
    print(f"Empréstimo negado. A prestação de R$ {prestacao:.2f} excede 30% do salário.")'''








