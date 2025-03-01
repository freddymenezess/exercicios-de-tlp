import funcoes.funcoes as f

# Pedindo uma ação do utilizador
acao = f.verificarOpcao()

# Exibindo a ação escolhida
match acao:
    case 1:
        # Adicionando um novo curso
        f.adicionarCurso()
    case 2:
        # Listando os cursos
        f.mostrarCursos()
    case 3:
        # Listando os alunos de cada curso
        f.mostrarCursosAlunos()