import os; os.system('cls' if os.name == 'nt' else 'clear')

estudantes = {}

for i in range(3):
    nome = input(f"Nome do {i+1} estudante: ")
    notas = int(input("Nota final: "))

    estudantes[nome] = notas

for nome, notas in estudantes.items():
    if notas >= 7:
        situacao = "Aluno Aprovado"
    elif notas >= 5:
        situacao = "Aluno em Recuperação"
    else:
        situacao = "Aluno Reprovado"
    
    print(f"{nome} : {situacao}")