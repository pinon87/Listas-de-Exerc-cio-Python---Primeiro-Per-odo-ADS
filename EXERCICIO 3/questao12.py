import os; os.system('cls' if os.name == 'nt' else 'clear')

produtos = {}

def cadastro(nome, preco, quantidade):
    produtos[nome] = {
        "preco" : preco,
        "quantidade" : quantidade
    }
    print(f"\nProduto cadastrado.")

def valor_total(nome):
    if nome in produtos:
        total = produtos[nome]["preco"] * produtos[nome]["quantidade"]
        return total

def consulta(nome):
    if nome in produtos:
        dados = produtos[nome]
        total = valor_total(nome)
        print(f"Preço do produto: {dados['preco']:.1f}")
        print(f"Quantidade do produto disponível em estoque: {dados['quantidade']} unidades")
        print(f"Valor total do produto em estoque: {total:.1f}")
    else:
        print("\nProduto não cadastrado")

def listar():
    if not produtos:
        print("Nenhum produto cadastrado")
    else:
        for nome, dados in produtos.items():
            print(f"Nome: {nome}\n Preço: {dados['preco']}\n Quantidade: {dados['quantidade']}")



while True:
    print("=== CADASTRO DE PRODUTOS ===")
    print("1 - Cadastrar um produto")
    print("2 - Calcular o valor total em estoque de um produto")
    print("3 - Consultar os dados de um produto")
    print("4 - Listar os produtos cadastrados")
    print("5 - Sair")
    print("============================")

    opcao = input("Opção escolhida: ")

    match opcao:
        case "1":
            nome = input("Nome do produto: ")
            if nome not in produtos:
                preco = float(input("Preço do produto (R$): "))
                quantidade = int(input("Quantidade do produto: "))
                
                cadastro(nome, preco, quantidade)
            else:
                print('Produto já está cadastrado')

        case "2":
            nome = input("Nome do produto: ")         
            total = valor_total(nome)
            if total != None:
                print(f"Valor total de {nome}: {total:.1f}R$")
            else:
                print("Produto não está cadastrado")

        case "3":
            nome = input("Nome do produto: ") 
            consulta(nome)

        case "4":
            listar()

        case "5":
            print('Encerrando...')
            break

        case _:
            print("Opção inválida")

    input("\nPressione ENTER para continuar")