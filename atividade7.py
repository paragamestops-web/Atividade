# SISTEMA DE CINEMA

# Função do menu
def menu():
    print("=== CINEMA PYTHON ===")
    print("1 - Vingadores")
    print("2 - Minecraft: O Filme")
    print("3 - Homem-Aranha")



# Função para escolher filme
def escolher_filme():
    opcao = input("Escolha o filme: ")

    if opcao == "1":
        return "Vingadores", 30

    elif opcao == "2":
        return "Minecraft: O Filme", 25

    elif opcao == "3":
        return "Homem-Aranha", 28

    else:
        print("Filme inválido!")
        return None, 0


# Função para calcular valor
def calcular_valor(preco, quantidade):
    total = preco * quantidade
    return total


# Função de pagamento
def pagamento():
    print("Formas de pagamento:")
    print("1 - Pix")
    print("2 - Cartão")
    print("3 - Dinheiro")

    forma = input("Escolha a forma de pagamento: ")

    if forma == "1":
        return "Pix"

    elif forma == "2":
        return "Cartão"

    elif forma == "3":
        return "Dinheiro"

    else:
        return "Forma inválida"


# Função para finalizar compra
def finalizar_compra(nome, filme, quantidade, total, forma_pagamento):
    print("=== COMPRA FINALIZADA ===")
    print("Cliente:", nome)
    print("Filme:", filme)
    print("Quantidade de ingressos:", quantidade)
    print("Valor total: R$", total)
    print("Pagamento:", forma_pagamento)
    print("Obrigado pela compra!")


# =========================
# PROGRAMA PRINCIPAL
# =========================

# Nome do cliente
nome = input("Digite seu nome: ")

# Mostrar menu
menu()

# Escolher filme
filme, preco = escolher_filme()

# Verificar se escolheu corretamente
if filme != None:

    # Quantidade de ingressos
    quantidade = int(input("Quantos ingressos deseja? "))

    # Calcular total
    total = calcular_valor(preco, quantidade)

    print("Valor total: R$", total)

    # Escolher pagamento
    forma_pagamento = pagamento()

    # Finalizar compra
    finalizar_compra(nome, filme, quantidade, total, forma_pagamento)

else:
    print("Encerrando sistema.")