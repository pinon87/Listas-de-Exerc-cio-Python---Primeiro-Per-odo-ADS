import os; os.system('cls' if os.name == 'nt' else 'clear')

quant_n=int(input("Digite quantos números serão informados: ")) 

soma=0
maior=0
menor=0

for i in range(1, quant_n+1):
    valor=int(input(f"Digite o {i} valor: ")) 

    soma+=valor
    media=soma/quant_n
    
    if i==1:
        maior=valor
        menor=valor
    else:
        if valor>maior:
            maior=valor
            
        if valor<menor:
            menor=valor

print(f"\nSoma: {soma}")
print(f"Média: {media:.1f}")
print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")  