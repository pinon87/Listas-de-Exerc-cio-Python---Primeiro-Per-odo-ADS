import os; os.system('cls' if os.name == 'nt' else 'clear')

quant=int(input("Quantidade de números informados: "))

maior=0
menor=0

for i in range(1, quant+1):
    numero=int(input(f"Digite o {i}º número: "))

    if i==1:
        maior=numero
        menor=numero
    else:
        if numero>maior:
            maior=numero
        if numero<menor:
            menor=numero

diferenca=maior-menor

print(f"\nMaior número: {maior}")
print(f"Menor número: {menor}")
print(f"Diferença entre eles: {diferenca}")    
