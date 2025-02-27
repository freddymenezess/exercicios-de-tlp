#Criando o dicionário com os produtos
produtos = {
    "relogio": 25000,
    "carteira": 2000,
    "bolsa": 12000,
    "sapatos": 14000,
    "bolachas" : 2000
}

# Garantindo que o usuário digite um preço válido
while True:
    # Recebe o preço procurado caso seja um int
    try:
        precoProcurado = int(input("Informe o preço do produto que deseja: "))
        break
    # Mensagem caso o valor seja inválido
    except ValueError:
        print("Preço inválido! Tente novamente.")

# Iterando sobre os preços
for produto, preco in produtos.items():
    # Verificando um preço identico
    if precoProcurado in produtos.values():
        print(f"Produto: {produto.capitalize()} | Preço: {preco:,.2f}KZ")
        break
    # Mostrando a mensagem caso o preço não seja encontrado
    else:
        print("Nenhum produto com este preço!")
        break