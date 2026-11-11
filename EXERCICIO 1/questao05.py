import os; os.system('cls' if os.name == 'nt' else 'clear')

produtividade=float(input("Digite a nota de produtividade do funcionário : "))
qualidade=float(input("Digite a nota de qualidade do funcionário : "))
presenca=int(input("Digite o percentual de presença do funcionário em % : "))

media=((produtividade+qualidade)/2)

if presenca<75:
    print("Desempenho comprometido por baixa frequência")
elif (media>=9) and (presenca>=90):
    print("Excelente")
elif (media>=7) and (presenca>=85):
    print("Bom")
elif (media>=5) and (presenca>=75):
    print("Regular")
else:
    print("Insatisfatório")