import os; os.system('cls' if os.name == 'nt' else 'clear')

estudante = {
    "Nome" : input("Nome do estudante: "),
    "Idade" : int(input("Idade do estudante: ")),
    "Curso" : input("Curso do estudante: ")
}

print("\nDADOS DO ALUNO")
for chave, valor in estudante.items():
    print(chave, ":", valor)
