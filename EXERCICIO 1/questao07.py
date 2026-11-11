import os; os.system('cls' if os.name == 'nt' else 'clear')

idade = int(input("Digite a idade do aluno: "))
media=float(input("Digite a média do aluno: "))
freq=float(input("Digite a frequência do aluno em % : "))

print("\nTipos de Curso:")
print("1. Graduação")
print("2. Técnico")
print("3. Pós-graduação")
curso = int(input("Escolha o tipo de curso [1] - [3]: ")) 

if freq<75:
     print("\nREPROVADO POR FALTA")
else:
 match curso:
    case 1:
        print("Graduação: ")      
        if media>=7 and freq>=75:
            print("\nAPROVADO")
        elif media>=5 and freq>=75: 
            print("\nRECUPERAÇÃO")
        else:
            print("\nREPROVADO") 
    case 2:
        print("Técnico: ")
        if media>=6 and freq>=75:
            print("\nAPROVADO")
        elif media>=4 and freq>=75: 
            print("\nRECUPERAÇÃO")
        else:
            print("\nREPROVADO") 
    case 3:
        print("Pós-Graduação: ")  
        if media>=7 and freq>=75:
            print("\nAPROVADO")
        else:
            print("\nREPROVADO") 
    case _:
        print("OPÇÃO INVÁLIDA")
    