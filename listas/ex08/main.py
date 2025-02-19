from random import sample as samp

lista = samp(range(1, 29), 10)

print(f"Lista: {lista}\n")

multiplier = int(input("Digite um número: "))
multiplied = [i * multiplier for i in lista]

print(f"\nLista multiplicada: {multiplied}")