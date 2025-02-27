alunos = {
    "João": {"idade": 14, "notas": [18.5, 12, 13]},
    "Maria": {"idade": 15, "notas": [15, 9, 11]},
    "Pedro": {"idade": 14, "notas": [17.5, 12, 7]},
    "António": {"idade": 17, "notas": [11.5, 9, 7]}
}

medias = {}
idades = []

#Inserindo todas as idades numa lista
for dados in alunos.values():
    idades.append(dados["idade"])

#Calculando a média das idades
totalIdades = len(idades)
somaIdades = sum(idades)
mediaIdades = int(somaIdades/totalIdades)

#Calculando a média das notas de cada um
for nome, dados in alunos.items():
    notas = dados["notas"]
    medias[nome] = float(f"{sum(notas) / len(notas):.2f}")

#Calculando a mediana das idades
idades.sort()
if totalIdades % 2 == 0:
    mediana = []
    primeiroIndice = totalIdades//2 - 1
    segundoIndice = totalIdades//2
    mediana.append(idades[primeiroIndice])
    mediana.append(idades[segundoIndice])
else:
    mediana = idades[totalIdades//2]

for nome, dados in alunos.items():
    print(f"{nome}: {dados}")

print("\nMédia dos Alunos")
for nome, media in medias.items():
    print(f"{nome}: {media}")

print(f"\nMédia das idades: {mediaIdades}\nMediana das idades: {mediana}")
