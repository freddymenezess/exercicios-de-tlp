import funcoes.funcoes as f

# Pedindo uma ação do utilizador
acao = f.verificarOpcao()

# Exibindo a ação escolhida
match acao:
    case 1:
        # Adicionando um novo curso
        while True:
            nomeNovoCurso = input("Digite o nome do curso: ")
            if nomeNovoCurso.replace(" ", "").isalpha():
                nomeValido = nomeNovoCurso
                f.adicionarCurso(nomeValido)
                break
            else:
                print("Nome do curso inválido! Tente novamente.")
                continue

    case 2:
        # Listando os cursos
        f.mostrarCursos()

    case 3:
        # Listando os alunos de cada curso
        f.cursosAlunos()

