import os; os.system('cls' if os.name == 'nt' else 'clear')

lista = [int(input(f"Digite o {i+1}º número: ")) for i in range(5)]

print(f"Lista completa: {lista}")

print(f"O maior número entre esses é: {max(lista)} e o menor é: {min(lista)}")

print(f"A soma desses números resulta em: {sum(lista)}")

print(f"A média desses números é: {(sum(lista) / 5)}")

print(f"A lista em ordem crescente fica da seguinte forma: {sorted(lista)}")