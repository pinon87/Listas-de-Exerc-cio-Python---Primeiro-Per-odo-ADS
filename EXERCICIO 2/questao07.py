import os; os.system('cls' if os.name == 'nt' else 'clear')

contador=0
contador_pos=0
contador_neg=0

for i in range(1,11):
    numeros=int(input(f"Digite o {i} números: "))

    if numeros<0:
        contador_neg+=1
    elif numeros>0:
        contador_pos+=1
    elif numeros==0:
        contador+=1

print(f"\n Quantidade de positivos: {contador_pos}")
print(f" Quantidade de negativos: {contador_neg}")
print(f" Quantidade de números iguais a zero: {contador}")