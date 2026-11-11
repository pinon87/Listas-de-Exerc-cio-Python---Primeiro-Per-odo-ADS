import os; os.system('cls' if os.name == 'nt' else 'clear')

print("\n======= OPÇÕES =======")
print("1. Cadastrar aluno")
print("2. Consultar aluno")
print("3. Alterar aluno")
print("4. Excluir aluno")
print("5. Listar alunos")
print("6. Sair")
print("======================")

opcao=int(input("Escolha uma opção de [1] a [6] : "))

match opcao:
    case 1:
        print("\n Cadastrar aluno")
    case 2:
        print("\n Consultar aluno")
    case 3:
        print("\n Alterar aluno")
    case 4:
        print("\n Excluir aluno")
    case 5:
        print("\n Listar alunos")
    case 6:
        print("\n Sair")
    case _:
        print("Opção inválida")