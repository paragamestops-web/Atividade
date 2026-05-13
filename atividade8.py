produtos = []
historico_vendas = []

usuario_correto = "admin"
senha_correta = "123"


def login():

    tentativas = 0

    while tentativas < 3:

        print("\n===== LOGIN =====")

        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario == usuario_correto and senha == senha_correta:
            print("\nLogin realizado com sucesso!")
            return True

        else:
            tentativas += 1
            print("Usuário ou senha incorretos.")
            print("Tentativas restantes:", 3 - tentativas)

    print("\nSistema bloqueado.")
    return False


def cadastrar_produto():

    print("\n===== CADASTRO DE PRODUTO =====")

    codigo = input("Código do produto: ")

    for produto in produtos:

        if produto[0] == codigo:
            print("Erro: código já cadastrado.")
            return

    nome = input("Nome do produto: ")

    preco = float(input("Preço do produto: "))

    if preco < 0:
        print("Erro: preço inválido.")
        return

    estoque = int(input("Quantidade em estoque: "))

    if estoque < 0:
        print("Erro: estoque inválido.")
        return

    novo_produto = [codigo, nome, preco, estoque, 0]

    produtos.append(novo_produto)

    print("Produto cadastrado com sucesso!")


def listar_produtos():

    print("\n===== LISTA DE PRODUTOS =====")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:

        print("----------------------------")
        print("Código:", produto[0])
        print("Nome:", produto[1])
        print("Preço: R$", produto[2])
        print("Estoque:", produto[3])
        print("Quantidade vendida:", produto[4])


def realizar_venda():

    print("\n===== REALIZAR VENDA =====")

    codigo = input("Digite o código do produto: ")

    for produto in produtos:

        if produto[0] == codigo:

            quantidade = int(input("Quantidade desejada: "))

            if quantidade <= 0:
                print("Quantidade inválida.")
                return

            if quantidade > produto[3]:
                print("Estoque insuficiente.")
                return

            total = quantidade * produto[2]

            produto[3] -= quantidade

            produto[4] += quantidade

            historico_vendas.append([
                produto[1],
                quantidade,
                total
            ])

            print("\n===== CUPOM FISCAL =====")
            print("Produto:", produto[1])
            print("Quantidade:", quantidade)
            print("Total: R$", total)

            print("\nVenda realizada com sucesso!")
# Esse "n "serve pra pular uma linha do código)
            return

    print("Produto não encontrado.")


def repor_estoque():

    print("\n===== REPOR ESTOQUE =====")

    codigo = input("Código do produto: ")

    for produto in produtos:

        if produto[0] == codigo:
# ordem do produto: [codigo, nome, preco, estoque, quantidade_vendida]
            quantidade = int(input("Quantidade para repor: "))

            if quantidade <= 0:
                print("Quantidade inválida.")
                return

            produto[3] += quantidade

            print("Estoque atualizado!")
            return

    print("Produto não encontrado.")


def pesquisar_produto():

    print("\n===== PESQUISAR PRODUTO =====")

    nome = input("Digite o nome do produto: ")

    encontrado = False

    for produto in produtos:

        if nome.lower() in produto[1].lower():

            print("----------------------------")
            print("Código:", produto[0])
            print("Nome:", produto[1])
            print("Preço: R$", produto[2])
            print("Estoque:", produto[3])

            encontrado = True

    if encontrado == False:
        print("Produto não encontrado.")


def alterar_preco():

    print("\n===== ALTERAR PREÇO =====")

    codigo = input("Código do produto: ")

    for produto in produtos:

        if produto[0] == codigo:

            novo_preco = float(input("Novo preço: "))

            if novo_preco < 0:
                print("Preço inválido.")
                return

            produto[2] = novo_preco

            print("Preço atualizado!")
            return

    print("Produto não encontrado.")


def relatorio():

    print("\n===== RELATÓRIO =====")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    mais_caro = produtos[0]

    for produto in produtos:

        if produto[2] > mais_caro[2]:
            mais_caro = produto

    maior_estoque = produtos[0]

    for produto in produtos:

        if produto[3] > maior_estoque[3]:
            maior_estoque = produto

    valor_total = 0

    for produto in produtos:
        valor_total += produto[2] * produto[3]

    quantidade_total = 0

    for produto in produtos:
        quantidade_total += produto[3]

    mais_vendido = produtos[0]

    for produto in produtos:

        if produto[4] > mais_vendido[4]:
            mais_vendido = produto

    print("Produto mais caro:", mais_caro[1])

    print("Produto com maior estoque:",
          maior_estoque[1])

    print("Valor total do estoque: R$",
          valor_total)

    print("Quantidade total em estoque:",
          quantidade_total)

    print("Produto mais vendido:",
          mais_vendido[1])

    print("\n===== HISTÓRICO DE VENDAS =====")

    if len(historico_vendas) == 0:
        print("Nenhuma venda realizada.")

    else:

        for venda in historico_vendas:

            print("----------------------")
            print("Produto:", venda[0])
            print("Quantidade:", venda[1])
            print("Total: R$", venda[2])


if login():

    while True:

        print("\n========================")
        print("     MERCADO PYTHON")
        print("========================")

        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Realizar venda")
        print("4 - Repor estoque")
        print("5 - Relatório")
        print("6 - Pesquisar produto")
        print("7 - Alterar preço")
        print("8 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()

        elif opcao == "2":
            listar_produtos()

        elif opcao == "3":
            realizar_venda()

        elif opcao == "4":
            repor_estoque()

        elif opcao == "5":
            relatorio()

        elif opcao == "6":
            pesquisar_produto()

        elif opcao == "7":
            alterar_preco()

        elif opcao == "8":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")