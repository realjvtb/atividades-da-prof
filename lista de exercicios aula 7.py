#exercício 1

'''pessoa = {"nome": "joao", "idade": 19, "cidade": "curitiba"}

print("Dicionário:", pessoa)

chave = input("Digite uma chave (nome / idade / cidade): ")

if chave in pessoa:
    print(f"Valor de '{chave}':", pessoa[chave])
else:
    print("Chave não encontrada no dicionário.")'''

#exercício 2

'''precos = {"maçã": 3.50, "banana": 2.00, "mamão": 7.30}

print("Tabela de preços:", precos)

produto = input("Qual produto deseja alterar? ")

if produto in precos:
    novo_preco = float(input(f"Novo preço para '{produto}': R$ "))
    precos[produto] = novo_preco
    print("Dicionário atualizado:", precos)
else:
    print("Produto não encontrado no dicionário.")'''

#exercício 3

'''cadastro = {}

nome = input("Digite um nome: ")
idade = int(input("Digite a idade: "))

cadastro[nome] = idade

print("Dicionário criado:", cadastro)'''

#exercício 4

'''chave1 = input("Digite a chave do par 1: ")
valor1 = input("Digite o valor do par 1: ")

chave2 = input("Digite a chave do par 2: ")
valor2 = input("Digite o valor do par 2: ")

chave3 = input("Digite a chave do par 3: ")
valor3 = input("Digite o valor do par 3: ")

dicionario = dict([(chave1, valor1), (chave2, valor2), (chave3, valor3)])

print("Dicionário criado com dict():", dicionario)'''

#exercício 5

'''dados = {"cor": "preto", "tamanho": "P", "marca": "olympikus"}

print("Dicionário atual:", dados)

resposta = input("Deseja apagar todos os dados? (sim/não): ")

if resposta == "sim":
    dados.clear()

print("Dicionário final:", dados)'''

#exercício 6

'''original = {"nome": "joao", "idade": 19, "curso": "design"}
copia = original.copy()

chave = input("Qual chave da cópia deseja alterar? (nome / idade / curso): ")
novo_valor = input(f"Novo valor para '{chave}': ")

copia[chave] = novo_valor

print("Original:", original)
print("Cópia:", copia)'''

#exercício 7

'''entrada = input("Digite nomes separados por vírgula: ")

nomes = [nome.strip() for nome in entrada.split(",")]

dicionario = dict.fromkeys(nomes, 0)

print("Dicionário criado com fromkeys():", dicionario)'''

#exercício 8

'''alunos = {"joao": 6.0, "carlos": 7.9, "corando": 8.3}

print("Alunos cadastrados:", list(alunos.keys()))

nome = input("Digite o nome do aluno: ")

nota = alunos.get(nome, "Aluno não encontrado no sistema.")

print(f"Resultado para '{nome}':", nota)'''

#exercício 9

'''produtos = {'feijao': 5.99, "arroz": 15.50, "macarrão": 4.99}

print("Chaves (keys)  :", list(produtos.keys()))
print("Valores (values):", list(produtos.values()))
print("Pares (items) :", list(produtos.items()))'''

#exercício 10

'''dados = {"João": 25, "Maria": 30, "Pedro": 20, "Lucas": 18}
print("Dicionário inicial:", dados)

# pop()
chave = input("Digite uma chave para remover com pop(): ")
removido = dados.pop(chave)
print(f"Removido com pop(): '{chave}' → {removido}")
print("Após pop():", dados)

# popitem()
item = dados.popitem()
print(f"Removido com popitem(): {item}")
print("Após popitem():", dados)

# update()
nova_chave = input("Nova chave para adicionar via update(): ")
novo_valor = int(input("Novo valor: "))
dados.update({nova_chave: novo_valor})

print("Dicionário final:", dados)'''

#exercício 11

usuarios = {"Alice": 30, "Bruno": 25, "Carla": 22}

opcao = ""

while opcao != "0":

    print("\n--- MENU ---")
    print("1  - Exibir todos os usuários")
    print("2  - Buscar usuário (get)")
    print("3  - Adicionar usuário")
    print("4  - Atualizar idade")
    print("5  - Remover usuário (pop)")
    print("6  - Remover último inserido (popitem)")
    print("7  - Criar cópia e alterar valor (copy)")
    print("8  - Inicializar com fromkeys")
    print("9  - Atualizar com outro dicionário (update)")
    print("10 - Limpar todos os dados (clear)")
    print("11 - Criar dicionário com dict() e tuplas")
    print("0  - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Nomes  (keys)  :", list(usuarios.keys()))
        print("Idades (values):", list(usuarios.values()))
        print("Pares  (items) :", list(usuarios.items()))

    elif opcao == "2":
        nome = input("Nome do usuário: ")
        resultado = usuarios.get(nome, "Usuário não encontrado.")
        print("Resultado:", resultado)

    elif opcao == "3":
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        usuarios[nome] = idade
        print("Usuário adicionado:", usuarios)

    elif opcao == "4":
        nome = input("Nome do usuário a atualizar: ")
        if nome in usuarios:
            nova_idade = int(input("Nova idade: "))
            usuarios[nome] = nova_idade
            print("Dicionário atualizado:", usuarios)
        else:
            print("Usuário não encontrado.")

    elif opcao == "5":
        nome = input("Nome do usuário a remover: ")
        if nome in usuarios:
            removido = usuarios.pop(nome)
            print(f"Removido: '{nome}' → {removido}")
            print("Dicionário:", usuarios)
        else:
            print("Usuário não encontrado.")

    elif opcao == "6":
        if usuarios:
            item = usuarios.popitem()
            print("Removido com popitem():", item)
            print("Dicionário:", usuarios)
        else:
            print("Dicionário vazio.")

    elif opcao == "7":
        if usuarios:
            copia = usuarios.copy()
            nome = input("Qual usuário da cópia deseja alterar? ")
            if nome in copia:
                nova_idade = int(input("Nova idade na cópia: "))
                copia[nome] = nova_idade
            print("Original:", usuarios)
            print("Cópia   :", copia)
        else:
            print("Dicionário vazio.")

    elif opcao == "8":
        entrada = input("Nomes separados por vírgula: ")
        nomes = [n.strip() for n in entrada.split(",")]
        idade_padrao = int(input("Idade padrão: "))
        novo_dic = dict.fromkeys(nomes, idade_padrao)
        print("Criado com fromkeys():", novo_dic)
        usuarios.update(novo_dic)
        print("Dicionário principal após update():", usuarios)

    elif opcao == "9":
        qtd = int(input("Quantos usuários informar? "))
        novos = {}
        for i in range(qtd):
            nome = input(f"  Nome {i + 1}: ")
            idade = int(input(f"  Idade {i + 1}: "))
            novos[nome] = idade
        usuarios.update(novos)
        print("Dicionário após update():", usuarios)

    elif opcao == "10":
        confirmacao = input("Tem certeza? (sim/não): ")
        if confirmacao == "sim":
            usuarios.clear()
            print("Dicionário limpo:", usuarios)

    elif opcao == "11":
        qtd = int(input("Quantos pares informar? "))
        tuplas = []
        for i in range(qtd):
            nome = input(f"  Nome {i + 1}: ")
            idade = int(input(f"  Idade {i + 1}: "))
            tuplas.append((nome, idade))
        novo = dict(tuplas)
        print("Criado com dict():", novo)
        substituir = input("Substituir o dicionário principal? (sim/não): ")
        if substituir == "sim":
            usuarios = novo
            print("Dicionário principal:", usuarios)

    elif opcao == "0":
        print("Encerrando. Até logo!")

    else:
        print("Opção inválida.")




