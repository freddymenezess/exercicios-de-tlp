def criar_matriz(linhas, colunas):
    """
    Cria uma matriz com dimensões fornecidas, pedindo os valores ao usuário.
    Retorna a matriz como lista de listas.
    """
    matriz = []
    print(f"Digite os valores para a matriz de {linhas}x{colunas}:")
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = float(input(f"Elemento [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def somar_linhas(matriz):
    """
    Retorna uma lista com a soma de cada linha da matriz.
    """
    return [sum(linha) for linha in matriz]

def somar_colunas(matriz):
    """
    Retorna uma lista com a soma de cada coluna da matriz.
    """
    colunas = len(matriz[0])
    somas = []
    for c in range(colunas):
        soma_coluna = 0
        for linha in matriz:
            soma_coluna += linha[c]
        somas.append(soma_coluna)
    return somas

def rotacionar_matriz_90_graus(matriz):
    """
    Rotaciona a matriz 90 graus no sentido horário.
    """
    transposta = list(zip(*matriz))
    matriz_rotacionada = [list(reversed(linha)) for linha in transposta]
    return matriz_rotacionada

def imprimir_matriz(matriz):
    """
    Imprime a matriz em formato legível.
    """
    for linha in matriz:
        print(linha)

def intersecao_listas(lista1, lista2):
    """
    Retorna a interseção entre lista1 e lista2.
    """
    return [item for item in lista1 if item in lista2]

def main_matriz_e_operacoes():
    print("==== MATRIZ E OPERAÇÕES BÁSICAS ====\n")

    # 1) Criação da matriz
    linhas = int(input("Quantas linhas terá a matriz? "))
    colunas = int(input("Quantas colunas terá a matriz? "))
    
    matriz = criar_matriz(linhas, colunas)

    print("\nMatriz digitada:")
    imprimir_matriz(matriz)

    # 2) Soma de linhas e colunas
    soma_linhas = somar_linhas(matriz)
    soma_colunas = somar_colunas(matriz)

    print("\nSoma de cada linha:", soma_linhas)
    print("Soma de cada coluna:", soma_colunas)

    # 3) Rotação da matriz (90 graus)
    matriz_rotacionada = rotacionar_matriz_90_graus(matriz)
    print("\nMatriz rotacionada 90 graus:")
    imprimir_matriz(matriz_rotacionada)

    # 4) Interseção entre duas listas fornecidas pelo usuário
    print("\n==== BUSCA DE ELEMENTOS EM LISTAS ====")
    lista1 = input("Digite valores para a primeira lista, separados por espaço: ").split()
    lista2 = input("Digite valores para a segunda lista, separados por espaço: ").split()

    lista_intersecao = intersecao_listas(lista1, lista2)
    print("Elementos presentes em ambas as listas:", lista_intersecao)


# Chamando a função principal automaticamente
main_matriz_e_operacoes()
