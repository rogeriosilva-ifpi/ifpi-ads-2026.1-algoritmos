from utils import obter_int_positivo

def main():
    soma = 0
    qtd_reprovados = 0
    qtd_recuperacao = 0
    qtd_aprovados = 0
    qtd_alunos = int(input('Quantos alunos? '))
    maior_nota = 0
    menor_nota = 10

    for i in range(1, qtd_alunos + 1):
        nota = float(input(f'Nota aluno {i}: '))
        soma += nota
        classif = classificacao(nota)
        print(classif)
        if classif == 'Aprovado':
            qtd_aprovados += 1
        elif classif == 'Recuperação':
            qtd_recuperacao += 1
        elif classif == 'Reprovado':
            qtd_reprovados += 1

        if nota > maior_nota:
            maior_nota = nota
        if nota < menor_nota:
            menor_nota = nota

    media = calc_media(soma, qtd_alunos)
    print(f'''Maior nota: {maior_nota}
Menor nota: {menor_nota}
Média da turma: {media}
Quantidade de alunos aprovados: {qtd_aprovados}
Quantidade de alunos reprovados: {qtd_reprovados}
Quantidade de alunos em recuperação: {qtd_recuperacao}''')




def calc_media(soma, qtd_alunos):
    media = soma / qtd_alunos
    return media


def classificacao(nota):
    if nota < 5:
        return 'Reprovado'
    elif nota < 7:
        return 'Recuperação'
    elif nota <= 10:
        return 'Aprovado'
    


if __name__ == "__main__":
    main()