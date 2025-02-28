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

def cursosAlunos():
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

def adicionarCurso(nomeCurso):
    from unidecode import unidecode
    nomeCurso = unidecode(nomeCurso.lower())
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