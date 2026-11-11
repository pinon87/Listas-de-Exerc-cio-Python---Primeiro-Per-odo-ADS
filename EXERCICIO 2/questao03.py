import os; os.system('cls' if os.name == 'nt' else 'clear')

n=int(input("Digite um número inteiro positivo: "))

soma=0

for i in range(1, n+1):
    soma+=i

print(f"\nSoma = {soma}")