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
            curso, alunos = linha.split(":")
            if not alunos:
                print(f"{corrigirPalavra(curso)}\nNenhum aluno.\n")
            else:
                print(f"{corrigirPalavra(curso)}\n{alunos.strip()}\n")


def mostrarCursos():
    with open("cursos.txt", "r", encoding="utf-8") as arquivo:
        print("\nCursos")
        for linha in arquivo:
            curso = linha.strip().split(":")[0]
            print(corrigirPalavra(curso))


def adicionarCurso(nomeCurso):
    cursos = []
    with open("cursos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            cursos.append(linha.strip().split(":")[0])
        if nomeCurso in cursos:
            print("Este curso já está na lista.")
        else:
            with open("cursos.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"{nomeCurso}: \n")