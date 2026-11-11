import os
os.system('cls' if os.name == 'nt' else 'clear')

media=float(input("Qual a média do aluno? "))
freq=float(input("Qual a frequência do aluno? "))
rendaf=float(input("Qual a renda familiar do aluno (R$)? "))
outra_bolsa=input("O aluno tem outra bolsa? (S/N): ").strip().upper()

elegibilidade=True

if media<7:
    print("Média insuficiente,logo:")
    elegibilidade=False
if freq<75:
    print("Frequência insuficiente,logo:")
    elegibilidade=False
if rendaf>3000:
    print("Renda acima do limite,logo:")
    elegibilidade=False
if outra_bolsa=="S" or outra_bolsa=="SIM":
    print("Já possui outra bolsa,logo:")
    elegibilidade=False

if elegibilidade:
    print("\nAluno ELEGÍVEL para a bolsa")
else:
    print("\nAluno INELEGÍVEL para a bolsa")