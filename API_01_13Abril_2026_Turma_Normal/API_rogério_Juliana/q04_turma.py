from utilitaros import inteiro,positivo

def main():
    quant_alunos = validador()
    for f in range(1,quant_alunos+1):
        mostrar(f)
    
def validador():
    quant_alunos = inteiro('quantidade de alunos: ')
    while quant_alunos < 0:
        print('quantidade não pode ser menor que 0...')
        quant_alunos = inteiro('quantidade de alunos: ')
    return quant_alunos

def notas(i):
    nota = positivo('insira a {i}° nota: ')
    return nota

def aprovacao(n):
    if n < 5:
        return 'reprovado'
    elif 5 >= n < 7:
        return 'recuperação'
    else:
        return 'aprovado'
    
def mostrar(f):
    nota = notas(f)
    situacaocao = aprovacao(nota)
    print(f'aluno {f}: nota - {nota} - {situacaocao}')

  


main()