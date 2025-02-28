def concatenar_listas(lista1, lista2):
    return lista1 + lista2

try:
    # Solicita ao usuário os elementos da primeira lista
    entrada_lista1 = input("Digite os elementos da primeira lista separados por espaço: ")
    lista1 = entrada_lista1.split()
    
    # Solicita ao usuário os elementos da segunda lista
    entrada_lista2 = input("Digite os elementos da segunda lista separados por espaço: ")
    lista2 = entrada_lista2.split()
    
    # Chama a função para concatenar as listas
    lista_concatenada = concatenar_listas(lista1, lista2)
    
    print("Lista concatenada:", lista_concatenada)
except Exception as e:
    print("Ocorreu um erro inesperado:", e)
