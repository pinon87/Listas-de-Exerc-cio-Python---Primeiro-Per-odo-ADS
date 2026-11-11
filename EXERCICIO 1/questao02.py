import os; os.system('cls' if os.name == 'nt' else 'clear')

preco=float(input("Qual o preço desse produto? "))
quant=int(input("Quanto desse produto tem no estoque? "))

if preco<=0:
    print("PREÇO INVÁLIDO ")
elif quant<0:
        print("QUANTIDADE INVÁLIDA ")
elif preco>1000 and quant<5:
    print("PRODUTO CARO COM ESTOQUE CRÍTICO")
elif preco>1000 and quant<=20:
    print("PRODUTO CARO COM ESTOQUE NORMAL")
elif preco>1000 and quant>20:
    print("PRODUTO CARO COM ESTOQUE ALTO")
elif preco<=1000 and quant<5:
    print("ESTOQUE CRÍTICO")
else:
    print("ESTOQUE NORMAL")