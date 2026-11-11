import os; os.system('cls' if os.name == 'nt' else 'clear')

dia = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabádo", "Domingo")

escolha = int(input("Digite um número de 1 a 7: "))

if 1<=escolha<=7:
    print(f"Na semana corresponde a: {dia[escolha-1]}")
else:
    print("Opção inválida!")

