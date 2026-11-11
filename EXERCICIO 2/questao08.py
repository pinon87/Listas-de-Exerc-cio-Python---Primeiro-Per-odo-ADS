import os; os.system('cls' if os.name == 'nt' else 'clear')

aprovados=0
reprovados=0
recuperacao=0
cadastrados=0

while True:
    nota=float(input("Digite a nota do estudante (-1 pra sair) : "))

    if nota==-1:
        break
 
    cadastrados+=1

    if nota>=7:
        aprovados+=1
    elif nota>=5:
        recuperacao+=1
    else:
        reprovados+=1

print(f"\nQuantidade de estudantes aprovados: {aprovados}")
print(f"Quantidade de estudantes em recuperação: {recuperacao}")        
print(f"Quantidade de estudantes reprovados: {reprovados}")
print(f"Quantidade de estudantes cadastrados: {cadastrados}")