import os; os.system('cls' if os.name == 'nt' else 'clear')

saldo=1000.00

while True:
    print("\n1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao=input("Escolha uma opção: ")

    if opcao=="1":
        print("Saldo atual: ","R$", saldo)
    elif opcao=="2":
        deposito=float(input("Digite o valor do depósito: "))
        if deposito>0:        
            saldo+=deposito
            print("Depósito realizado com sucesso!")  
        else:
            print("Valor inválido")    
    elif opcao=="3":
        saque=float(input("Digite o valor que deseja sacar: ")) 
        if saque>saldo:
            print("Saldo insuficiente")
        elif saque<=0:
            print("Valor inválido")    
        else:
            saldo-=saque
            print("Saque realizado com sucesso!")
    elif opcao=="4":
        print("Sessão encerrada")
        break
    else:
        print("Opção inválida (1 - 4)") 
     