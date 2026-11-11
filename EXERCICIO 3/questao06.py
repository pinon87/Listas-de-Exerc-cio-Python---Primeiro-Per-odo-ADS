import os; os.system('cls' if os.name == 'nt' else 'clear')

valores = (5, 8, 3, 8, 2, 8, 10, 3)

print(f"Quantidade total de elementos: {len(valores)}")

print(f"O maior valor: {max(valores)} | O menor valor: {min(valores)}")

print(f"Quantas vezes o número 8 aparece: {valores.count(8)}")

print(f"Posição da primeira ocorrência do 3: {valores.index(3)}")

print(f"Nova tupla com ordem invertida: {valores[::-1]}")
