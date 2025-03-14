def pangrama(frase):
    alfabeto = set("abcdefghijklmnopqrstuvwxyz")
    letras_na_frase = {char for char in frase.lower() if char.isalpha()}
    return alfabeto.issubset(letras_na_frase)

frase = input("Insira uma frase para verificar se é um pangrama: ")

if pangrama(frase):
    print(f"A frase '{frase}' é um pangrama.")
else:
    print(f"A frase '{frase}' não é um pangrama.")
