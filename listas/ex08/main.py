def multiplicar_lista(lista, fator):
    return [elemento * fator for elemento in lista]

try:
    # Entrada da lista
    lista = list(map(float, input("Digite os números da lista separados por espaço: ").split()))
    
    # Entrada do fator de multiplicação
    fator = float(input("Digite o número pelo qual deseja multiplicar a lista: "))
    
    # Multiplicação e exibição do resultado
    resultado = multiplicar_lista(lista, fator)
    print("Lista resultante:", resultado)

except ValueError:
    print("Erro: Por favor, insira apenas números válidos.")
