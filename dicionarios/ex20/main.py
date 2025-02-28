from typing import final

cursos = {
    "Informática" : ["João", "Armindo", "Isabel", "Augusto"],
    "Mecânica" : ["André", "Jucília", "Josemar", "Armindo"],
    "Construção Civíl" : ["Felipe", "André", "Andrade", "Correia"]
}

# Mostrando os cursos e alunos listados
for curso, alunos in cursos.items():
    print(f"Alunos do curso de {curso}\n{alunos}\n")

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
            try:
                novoCurso = input("Digite o nome do curso: ")
                cursos[novoCurso] = []
                print(f"Curso de {novoCurso} adicionado!")
                break
            except ValueError:
                print("Opção inválida! Tente novamente.")
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

# Mensagem final
final(print("\nObrigado pela preferência!"))