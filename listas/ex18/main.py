def remover_duplicatas(lista):
    """
    Remove os elementos duplicados de uma lista, mantendo a ordem original.
    Retorna a nova lista sem duplicatas.
    """
    lista_sem_duplicatas = []
    for item in lista:
        if item not in lista_sem_duplicatas:
            lista_sem_duplicatas.append(item)
    return lista_sem_duplicatas

def main_remocao_duplicatas():
    print("==== REMOÇÃO DE DUPLICATAS ====")

    # Entrada da lista fornecida pelo usuário
    lista = input("Digite os elementos da lista separados por espaço: ").split()

    # Chamada da função para remover duplicatas
    lista_sem_duplicatas = remover_duplicatas(lista)

    # Exibição do resultado
    print("\nLista sem duplicatas:", lista_sem_duplicatas)


# Chamando a função principal automaticamente
main_remocao_duplicatas()
