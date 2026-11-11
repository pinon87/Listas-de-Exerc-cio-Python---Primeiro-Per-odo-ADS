import os; os.system('cls' if os.name == 'nt' else 'clear')

idade=int(input("Digite sua idade: "))

if idade<0:
    print("IDADE INVÁLIDA ")
elif idade<=12:
    print("CRIANÇA")
elif  idade<=17:
    print("ADOLESCENTE")
elif idade<=59:
    print("ADULTO")
else:
    print("IDOSO")

    
