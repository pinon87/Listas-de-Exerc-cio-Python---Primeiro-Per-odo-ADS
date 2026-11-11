import os; os.system('cls' if os.name == 'nt' else 'clear')

n=int(input("Digite um número inteiro positivo: "))

for i in range(1, 11):
    print(f"{n} X {i} = {n*i} ")
   