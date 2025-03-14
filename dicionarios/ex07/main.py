# Importando o módulo collections
from collections import Counter

# Removendo os espaços da string
string = input("Digite uma palavra: ").replace(" ", "")

# Contando o número de vezes que cada letra aparece na string e armazenando em uma tupla
contagem = Counter(string)

# Transformando a tupla em um dicionário
dicionario = dict(contagem)

# Printando cada ocorrência
for letra, vezes in dicionario.items():
    print(f"{letra}: {vezes} vez (es)")
