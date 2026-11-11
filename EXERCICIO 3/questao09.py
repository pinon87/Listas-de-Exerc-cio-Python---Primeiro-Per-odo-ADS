import os; os.system('cls' if os.name == 'nt' else 'clear')

estoque = {}

while True:
    print("= Controle de Estoque =")
    print("1 - Cadastro de mercadoria")
    print("2 - Atualizar quantidade de um produto")
    print("3 - Consultar quantidade disponível")
    print("4 - Exibir todos os produtos")
    print("5 - Encerrar")

    opcao = input("\nEscolha uma das opções (1-5): ")

    match opcao:
        
        case "1": #CADASTRO
            produto = input("Nome do produto a ser cadastrado: ")
            if produto in estoque:
                print("O produto já está no sistema")
            else:
                quantidade = int(input("Quantidade disponível do produto: "))
                estoque[produto] = quantidade
                print("Produto cadastrado")

        case "2" : #ATUALIZAÇÃO
            produto = input("Nome do produto a ser atualizado: ")  
            if produto in estoque:
                quantidade_nova = int(input(f"Quantidade atualizada do {produto}: "))
                estoque[produto] = quantidade_nova 
                print("Produto atualizado")       
            else:
                print("Produto não está no sistema")

        case "3": #CONSULTA
            produto = input("Nome do produto a ser consultado: ")
            if produto in estoque:
                print(f"Quantidade de {produto} em estoque: {estoque[produto]} unidades")
            else:
                print("Produto não está no sistema")

        case "4": #EXIBIR
            print("\n= Todos os produtos em estoque =")
            if not estoque:
                print("Nenhum produto cadastrado") 
            else:
                for produto, quantidade in estoque.items():
                    print(f"{produto} : {quantidade} unidades")   

        case "5": #ENCERRAMENTO
            print("\nEncerrando...")
            break

        case _:
            print("\nOpção inválida")