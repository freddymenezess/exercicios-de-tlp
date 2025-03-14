# Criando o dicionário com os produtos
produtos = {
    "relógio": 25000,
    "carteira": 2500,
    "bolsa": 12000,
    "sapatos": 14000,
    "bolachas" : 2000
}

mesmos_precos = {}
precos_proximos = {}

# Garantindo que o usuário digite um preço válido
while True:
    # Recebendo o preço procurado caso seja um int
    try:
        preco_procurado = int(input("Informe o preço do produto que deseja: "))
        break
    # Mensagem caso o valor seja inválido
    except ValueError:
        print("Preço inválido! Tente novamente.")

# Iterando sobre os preços
for produto, preco in produtos.items():
    # Verificando se o preço é identico
    if preco_procurado == preco:
        mesmos_precos[produto] = preco
    else:
        if preco_procurado > preco and (preco_procurado - preco) <= 2500:
            precos_proximos[produto] = preco
            continue

if mesmos_precos:
    print(f"Produto: {produto.capitalize()} | Preço: {preco:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") + "KZ")
elif precos_proximos:
    print("Nenhum produto com este preço!\nProdutos com preços aproximados: ")
    for produto, preco in precos_proximos.items():
        print(f"Produto: {produto.capitalize()} | Preço: {preco:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") + "KZ")
else:
    print("Nenhum produto com este preço!")