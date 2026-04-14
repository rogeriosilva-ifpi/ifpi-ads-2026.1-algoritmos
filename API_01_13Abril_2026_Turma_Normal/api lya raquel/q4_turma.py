def main():
    qtd_alunos = int(input('Quantidade de alunos: '))

    total_aluno = qtd_alunos
    nota_maior = 0
    nota_menor = 5
    somatorio_notas = 0
    qtd_aprovado = 0
    qtd_recuperacao = 0
    qtd_reprovado = 0
    while qtd_alunos > 0:
        nota = float(input('Digite a nota: '))
        qtd_alunos -= 1
        somatorio_notas += nota
        if nota >= 7:
            print('Aluno aprovado!')
            qtd_aprovado += 1
            if nota > nota_maior:
                nota_maior = nota
        if nota >= 5 and nota < 7:
            print('Aluno em recuperação!')
            qtd_recuperacao += 1
        if nota < 5:
            print('Aluno reprovado!')
            qtd_reprovado += 1
            if nota < nota_menor:
                nota_menor = nota

    media = somatorio_notas / total_aluno

    tela = f'''
    Maior nota: {nota_maior}
    Menor nota: {nota_menor}
    Média: {media:.2f}
    Quantidade de Aprovados: {qtd_aprovado}
    Quantidade de Recuperação: {qtd_aprovado}
    Quantidade de Reprovados: {qtd_aprovado}
'''
    print(tela)
main()