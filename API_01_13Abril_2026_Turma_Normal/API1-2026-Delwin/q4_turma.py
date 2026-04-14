from utils import obterInteiro

def Main():
    #Chamando obter inteiro para pedir número 
    n = obterInteiro('Digite o número de alunos: ')

    #Variáveis utilitárias
    maior_nota = 0
    menor_nota = 0
    soma_notas = 0
    quant_aprovado = 0
    quant_recu = 0
    quant_reprovado = 0

    #Pedindo e processando as notas dos alunos:
    for i in range(n):
        nota = obterInteiro('Digite a nota do aluno (0 a 10): ')

        #Classificando as notas
        if nota >= 7:
            print('Aprovado!')
            soma_notas += nota
            quant_aprovado += 1
        elif nota >= 5:
            print('Recuperação!')
            soma_notas += nota
            quant_recu += 1
        else:
            print('Reprovado!')
            soma_notas += nota
            quant_reprovado += 1

        #Verificando se é maior ou menor nota
        if nota > maior_nota:
            maior_nota = nota
        if nota < menor_nota:
            menor_nota = nota

    #Mostrando resultados
    print(f'Maior nota: {maior_nota}')
    print(f'Menor nota: {menor_nota}')
    print(f'Média da turma: {soma_notas / n}')
    print(f'Alunos aprovados: {quant_aprovado}')
    print(f'Alunos de recuperação: {quant_recu}')
    print(f'Alunos reprovados: {quant_reprovado}')


Main()