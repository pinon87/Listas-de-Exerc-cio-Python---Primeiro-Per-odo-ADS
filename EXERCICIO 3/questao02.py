import os; os.system('cls' if os.name == 'nt' else 'clear')

lista = [int(input(f"Digite o {i+1}º número: ")) for i in range(10)]

numero = int(input("Digite o número a ser procurado na lista: "))

if numero in lista:
    print("Está Presente")
    
    quantidade = lista.count(numero)
    print(f"{quantidade} vezes!")

    posicoes = []
    for i in range(len(lista)):
        if lista[i] == numero:
            posicoes.append(i)

    print(f"Nas posições: {posicoes}")  

else:
    print("Não está presente")
