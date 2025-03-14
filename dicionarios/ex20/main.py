import funcoes.funcoes as f
from unidecode import unidecode

# Pedindo uma ação do utilizador
while True:
    try:
        opcao = int(input("1. Adicionar Cursos\n2. Listar Cursos\n3. Listar alunos em cada curso\n"))
        break
    except ValueError:
        print("Opção inválida! Tente novamente.")
        continue

# Exibindo a ação escolhida
match opcao:
    case 1:
        # Adicionando um novo curso
        while True:
            nomeNovoCurso = input("Digite o nome do curso: ")
            if nomeNovoCurso.replace(" ", "").isalpha():
                nomeNovoCurso = unidecode(nomeNovoCurso.strip().lower())
                f.adicionarCurso(nomeNovoCurso)
                break
            else:
                print("Nome do curso inválido! Tente novamente.")
                continue

    case 2:
        # Listando os cursos
        f.mostrarCursos()
    case 3:
        # Listando os alunos de cada curso
        f.mostrarCursosAlunos()