import os; os.system('cls' if os.name == 'nt' else 'clear')

lista = [int(input(f"Digite o {i+1}º número: ")) for i in range(10)]

pares = []
impares = []

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Lista original com {len(lista)} elementos: {lista}")
print(f"Lista apenas com números pares com {len(pares)} elementos: {pares}")
print(f"Lista apenas com números ímpares com {len(impares)} elementos: {impares}")
    