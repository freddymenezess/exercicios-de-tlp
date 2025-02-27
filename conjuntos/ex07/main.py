def pangrama(frase):
    frase = frase.lower()
    letras_na_frase = set(frase)
    return alfabeto.issubset(letras_na_frase)

frase = input("Insira uma frase para verificar se é um pangrama: ")

if pangrama(frase):
    print("A frase é um pangrama.")
else:
    print("A frase não é um pangrama.")
