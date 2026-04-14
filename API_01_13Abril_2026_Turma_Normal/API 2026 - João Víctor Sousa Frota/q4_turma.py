import os
from utils.os_utils import limpar_tela
from utils.number_utils import obter_inteiro, obter_float


def obter_notas():
    maior_nota = 0
    menor_nota = 10
    media_turma = 0
    aprovados = 0
    recuperacao = 0
    reprovados = 0
    print("Insira a quantidade de alunos que serão avaliados: ", end="")
    quantidade = obter_inteiro()
    for i in range(quantidade):
        print(f"Insira a nota do aluno {i + 1}: ", end="")
        nota = obter_float()
        resultado = verificar_aprovacao(nota)
        if resultado == 'aprovado':
            aprovados += 1
            if nota > maior_nota:
                maior_nota = nota
            if nota < menor_nota:
                menor_nota = nota
            media_turma += nota
        elif resultado == 'recuperação':
            recuperacao += 1
            if nota > maior_nota:
                maior_nota = nota
            if nota < menor_nota:
                menor_nota = nota
            media_turma += nota
        elif resultado == 'reprovado':
            reprovados += 1
            if nota > maior_nota:
                maior_nota = nota
            if nota < menor_nota:
                menor_nota = nota
            media_turma += nota
    media_turma = media_turma / quantidade
    return maior_nota, menor_nota, media_turma, aprovados, recuperacao, reprovados


def verificar_aprovacao(nota):
    if nota >= 7:
        resultado = 'aprovado'
    elif nota >= 5 and nota < 7:
        resultado = 'recuperação'
    elif nota < 5:
        resultado = 'reprovado'
    elif nota > 10 or nota < 0:
        print("Valor inválido, tente novamente.")
        resultado = 'inválido'
    return resultado


def exibir_dados(maior_nota, menor_nota, media_turma, aprovados, recuperacao, reprovados):
    print(f"""
    Maior nota: {maior_nota}
    Menor nota: {menor_nota}
    Média da turma: {media_turma}
    Quantidade de alunos aprovados: {aprovados}
    Quantidade de alunos de recuperação: {recuperacao}
    Quantidade de alunos reprovados: {reprovados}
    """)


def main():
    limpar_tela()
    maior_nota, menor_nota, media_turma, aprovados, recuperacao, reprovados = obter_notas()
    exibir_dados(maior_nota, menor_nota, media_turma, aprovados, recuperacao, reprovados)


main()