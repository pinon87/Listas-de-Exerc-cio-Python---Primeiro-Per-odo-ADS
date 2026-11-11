import os; os.system('cls' if os.name == 'nt' else 'clear')

lista = [int(input(f"Digite o {i+1}º número: ")) for i in range(10)]

repetidos = []

for numero in lista:
    if numero not in repetidos:
        repetidos.append(numero)

print(f"Lista original: {lista}")
print(f"Sem repetições: {repetidos}")