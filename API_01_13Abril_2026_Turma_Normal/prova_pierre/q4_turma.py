def main():
    menor_nota = None
    maior_nota = 0
    somatorio = 0
    contador = 0
    aprovados = 0
    recuperacao = 0
    reprovado = 0
    nota = 0

    def situacao(nota):
        if nota < 5:
            return 'Reprovado'
        elif nota < 7:
            return 'Recuperação'
        else:
            return 'Aprovado'


    n = int(input('Quantidade de alunos:' ))

    while contador < n:
        contador += 1
        nota = float(input(f'Nota do aluno {contador}: '))
        somatorio += nota

        situacao_aluno = situacao(nota)
        print(situacao_aluno)
        if situacao_aluno == 'Reprovado':
            reprovado += 1
        elif situacao_aluno == 'Recuperação':
            recuperacao += 1
        else:
            aprovados += 1


        if menor_nota == None:
            menor_nota = nota

        if nota < menor_nota:
            menor_nota = nota
        if nota > maior_nota:
            maior_nota = nota

    media = somatorio / n
    
    print(f'Menor nota: {menor_nota:.2f}\nMaior nota: {maior_nota:.2f}\nMédia das notas: {media:.2f}')
    print(f'Quantidade de reprovados: {reprovado}\nQuantidade em recuperação: {recuperacao}\nQuantidade de aprovados: {aprovados}')



main()