from utils_io import limpar_tela

def main():
    limpar_tela()

    n_alunos=int(input('Insira a quantidade de alunos que deseja ler as notas: '))
    soma_notas=0
    reprovados=0
    recuperacao=0
    aprovados=0
    for i in range(n_alunos):
        nota = float(input('Insira a nota do aluno:'))
        if nota<5:
            print('Reprovado')
            reprovados+=1
        elif nota<7:
            print('Recuperação')
            recuperacao+=1
        elif nota <=10:
            print('Aprovado')
            aprovados+=1
        soma_notas+=nota
    media_turma=soma_notas/n_alunos
    print(f'Média da turma: {media_turma:.1f}')
    print(f'Total de reprovados: {reprovados}')
    print(f'Total de alunos em recuperação: {recuperacao}')
    print(f'Total de aprovados: {aprovados}')

main()