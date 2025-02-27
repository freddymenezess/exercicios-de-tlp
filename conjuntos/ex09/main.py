meu_conjunto = set()
while True:
    entrada = input("Digite um valor para adicionar ao conjunto (ou 'sair' para terminar): ")
    if entrada.lower() == 'sair':
        break
    meu_conjunto.add(entrada)
print("Elementos do conjunto:")
for elemento in meu_conjunto:
    print(elemento)
