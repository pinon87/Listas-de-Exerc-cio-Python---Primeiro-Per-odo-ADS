import os; os.system('cls' if os.name == 'nt' else 'clear')

n=int(input("Digite um número inteiro positivo: "))

contador = 0

print("\nNúmeros pares: ")
for i in range(2, n+1, 2):
    print(i)
    contador += 1

print(f"Quantidades de números pares: {contador}")      
           