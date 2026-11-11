import os; os.system('cls' if os.name == 'nt' else 'clear')

aluno = {}

def cadastrar_aluno(nome, notas):
    aluno[nome] = notas
    print("\nAluno cadastrado")

def calcular_media(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)

def situacao_aluno(media):
    if media >= 7.0:
        return "Aprovado"
    else:
        return "Reprovado"

def listar_resultados():
    print("\n= RESULTADOS DA TURMA =")
    if not aluno:
        print("Nenhum aluno cadastrado")
        return
    aprovados = 0
    reprovados = 0

    for nome, notas in aluno.items():
        media = calcular_media(notas)
        situacao = situacao_aluno(media)

    if situacao == "Aprovado":
        aprovados += 1
    else:
        reprovados +=1

    print(f"Nome: {nome} | Notas: {notas} | Média: {media} | Situação: {situacao}")

    print(f"Total de aprovados: {aprovados}")
    print(f"Total de reprovados: {reprovados}")

    while True:
        print