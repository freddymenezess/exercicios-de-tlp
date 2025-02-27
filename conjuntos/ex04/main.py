# Solicitar os elementos do conjunto A ao usuário

elementos_A = input("Insira os elementos do conjunto A separados por espaço: ")

# Dividir a string de entrada em uma lista de elementos e convertê-la em um conjunto

conjunto_A = set(elementos_A.split())

print(f"Conjunto A: {conjunto_A}")

# Solicitar os elementos do conjunto B ao usuário

elementos_B = input("Insira os elementos do conjunto B separados por espaço: ")

# Dividir a string de entrada em uma lista de elementos e convertê-la em um conjunto

conjunto_B = set(elementos_B.split())

print(f"Conjunto B: {conjunto_B}")

# Encontrar a interseção dos conjuntos A e B

intersecao = conjunto_A & conjunto_B

print(f"Interseção dos conjuntos A e B: {intersecao}")
