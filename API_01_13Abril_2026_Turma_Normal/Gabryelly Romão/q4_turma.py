n = int(input('Digite a nota dos alunos: '))
for i in range(0, 11,n):
    if i >= 7:
        print('Aluno aprovado')
    elif i <=5 and i < 7:
        print('Recuperação')
    else:
        print('reprovado')
