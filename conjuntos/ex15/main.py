elementos_A = input("Insira os elementos da lista A separados por espaço: ")

conjunto_A = set(elementos_A.split())

print(f"Lista A: {conjunto_A}")

elementos_B = input("Insira os elementos da lista B separados por espaço: ")

conjunto_B = set(elementos_B.split())

print(f"Lista B: {conjunto_B}")

exclusivos_A = conjunto_A - conjunto_B

exclusivos_B = conjunto_B - conjunto_A

print(f"Elementos exclusivos da lista A: {exclusivos_A}")

print(f"Elementos exclusivos da lista B: {exclusivos_B}")
