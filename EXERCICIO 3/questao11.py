import os; os.system('cls' if os.name == 'nt' else 'clear')

def filtrar_pares(numeros):
    lista_pares = []
    for num in numeros:
        if num % 2 == 0:
            lista_pares.append(num)
    return lista_pares

lista = []
quantidade = int(input("Digite quantos números deseja: "))

for i in range(quantidade):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    lista.append(numero)

pares = filtrar_pares(lista)

print(f"\nLista original: {lista}")
print(f"Lista apenas com números pares: {pares}")

    