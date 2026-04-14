def main():
    alunos = int(input('Alunos(n°): '))
    aprovados = 0
    reprovados = 0
    recuperacao= 0
    soma = 0
    if alunos < 10:
        for i in range(1,alunos+1):
            nota = float(input('Nota: '))
            if nota >= 7:
                print('Aprovado!')
                aprovados += 1
            elif 5 <= nota < 7:
                print('Recuperação!')
                recuperacao += 1
            else:
                print('Reprovado!')
                reprovados += 1
            soma += nota
    print(f'Média da turma: {soma / alunos}')
    print(f'Aprovados:{aprovados} ')
    print(f'Reprovados: {reprovados}')
    print(f'Recuperacação: {recuperacao}')





main()