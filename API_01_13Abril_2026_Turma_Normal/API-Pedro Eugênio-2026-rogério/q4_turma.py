def turma():
    maior_nota=0
    menor_nota=0
    somatorio=0
    aprovado=0
    recuperaçao=0
    reprovado=0

    N_alunos=int(input('Digite a quatidade de alunos: '))
    for i in range(1, N_alunos+1):
        nota=float(input(f'Nota do {i}º aluno: '))
        somatorio+=nota
        if nota>=7:
            aprovado+=1
            print('esse aluno está aprovado !')
        elif 5<=nota<7:
            recuperaçao+=1
            print('esse alluno está de recuperação !')
        else:
            reprovado+=1
            print('esse aluno está reprovado! ')
        
        if nota>maior_nota:
            maior_nota=nota
        elif nota<menor_nota:
            menor_nota=nota
    

    print(f'a maior nota foi {maior_nota} e a menor nota foi {menor_nota}')
    print(f'a média da turma foi igual a: {somatorio/N_alunos:.1f}')
    print(f' {aprovado} foram aprovados, {recuperaçao} ficaram de recuperação e {reprovado} foram reprovados')

        
