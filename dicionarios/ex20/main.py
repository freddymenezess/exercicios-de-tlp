cursos = {
    "Informática" : ["João", "Armindo", "Isabel", "Augusto"],
    "Mecânica" : ["André", "Jucília", "Josemar", "Armindo"],
    "Construção Civíl" : ["Felipe", "André", "Andrade", "Correia"]
}
# Escrevendo os cursos e alunos num arquivo txt
with open("cursos.txt", "w", encoding="utf-8") as arquivo:
    for curso, alunos in cursos.items():
        arquivo.write(f"{curso}: {', '.join(alunos)}\n")

# Pedindo uma ação do usuário
while True:
    try:
        acao = int(input("1. Adicionar Cursos\n2. Listar Cursos\n3. Listar alunos em cada curso\n"))
        break
    except ValueError:
        print("Opção inválida! Tente novamente.")
        continue

# Exibindo a ação escolhida
match acao:
    case 1:
        # Adicionando um novo curso
        while True:
            novoCurso = input("Digite o nome do curso: ")
            if novoCurso.strip().isalpha():
                cursos[novoCurso] = []
                print(f"Curso de {novoCurso} adicionado!")
                break
            elif novoCurso == "":
                print("O nome do curso não pode estar vazio. Tente novamente.")
                continue
            elif novoCurso in cursos.keys():
                print("Este curso já existe! Tente novamente.")
                continue
            else:
                print("Nome do curso inválido! Tente novamente.")
                continue

    case 2:
        # Listando os cursos
        print("Cursos:")
        for curso in cursos.keys():
            print(curso)

    case 3:
        # Listando os alunos de cada curso
        for curso, alunos in cursos.items():
            print(f"Alunos do curso de {curso}\n{alunos}\n")
