import os; os.system('cls' if os.name == 'nt' else 'clear')

def calcular_media(notas):
    return (sum(notas) / 4)

lista = []

for i in range(4):
    notas = float(input(f"Digite a nota da AV{i+1}: "))
    lista.append(notas)

media = calcular_media(lista)

print(f"\nMédia: {media:.1f}")
