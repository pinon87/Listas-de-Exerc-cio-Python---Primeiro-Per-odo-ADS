import os; os.system('cls' if os.name == 'nt' else 'clear')

idade=int(input("Digite a idade do cliente: "))
salario=float(input("Digite quanto o cliente recebe de salário : "))
tempo_trab=float(input("Digite quantos anos o cliente tem de trabalho : "))
valor_solicitado=float(input("Digite o valor do empréstimo solicitado pelo cliente : "))

if idade<18:
    print("\nEMPRÉSTIMO NÃO PERMITIDO POR IDADE")
elif salario<1500:
    print("\nRENDA INSUFICIENTE")   
elif tempo_trab<1:
    print("\nTEMPO DE TRABALHO INSUFICIENTE")
elif valor_solicitado>(salario*10):
    print("\nVALOR SOLICITADO MUITO ALTO")
else:
    print("\nEMPRÉSTIMO PRÉ APROVADO")  
  

