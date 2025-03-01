def corrigirPalavra(palavra):
    from spellchecker import SpellChecker

    spell = SpellChecker(language="pt")
    palavra = palavra.strip()
    if not " " in palavra:
        if palavra in spell:
            palavraCorreta = palavra.capitalize()
            return palavraCorreta
        else:
            palavraCorreta = spell.correction(palavra).capitalize()
            return palavraCorreta
    else:
        palavras = palavra.split()
        palavrasCorrigidas = []
        for palavra in palavras:
            if palavra in spell:
                palavraCorreta = palavra.capitalize()
                palavrasCorrigidas.append(palavraCorreta)
            else:
                palavraCorreta = spell.correction(palavra).capitalize()
                palavrasCorrigidas.append(palavraCorreta)
        return " ".join(palavrasCorrigidas)


def mostrarCursosAlunos():
    with open("cursos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            curso, alunos = linha.strip().split(": ")
            return print(f"{corrigirPalavra(curso)}\n{alunos}\n")


def mostrarCursos():
    with open("cursos.txt", "r", encoding="utf-8") as arquivo:
        print("\nCursos")
        for linha in arquivo:
            curso = linha.strip().split(":")[0]
            print(corrigirPalavra(curso))


def adicionarCurso():
    from unidecode import unidecode

    while True:
        nomeNovoCurso = input("Digite o nome do curso: ")
        if nomeNovoCurso.replace(" ", "").isalpha():
            nomeCurso = unidecode(nomeNovoCurso.lower().strip())
            break
        else:
            print("Nome do curso inválido! Tente novamente.")
            continue

    cursos = []
    with open("cursos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            cursos.append(linha.strip().split(":")[0])
        if nomeCurso in cursos:
            print("Este curso já está na lista.")
        else:
            with open("cursos.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"{nomeCurso}: \n")


def verificarOpcao():
    while True:
        try:
            opcao = int(input("1. Adicionar Cursos\n2. Listar Cursos\n3. Listar alunos em cada curso\n"))
            return opcao

        except ValueError:
            print("Opção inválida! Tente novamente.")
            continue