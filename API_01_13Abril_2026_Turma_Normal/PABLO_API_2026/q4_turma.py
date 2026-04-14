from utils import *

def main():
    maior_nota = 0
    menor_nota = 10
    quant_alunos = 0
    quant_aprovados = 0
    quant_reprovados = 0
    quant_recuperacao = 0
    somatorio_notas = 0
    
    while True:
        nome = input('nome: ')
        
        if nome == '':
            break
        
        nota = obter_real_intervalo('nota: ', 0, 10)
        
        quant_alunos += 1
        somatorio_notas += nota
        maior_nota = obter_maior(nota, maior_nota)
        menor_nota = obter_menor(nota, menor_nota)
        
        if nota >= 7:
            quant_aprovados += 1
        elif nota >= 5:
            quant_recuperacao += 1
        else:
            quant_reprovados += 1
            
    try:
        print(f'Média da turma: {somatorio_notas / quant_alunos}')
        print(f'Maior nota: {maior_nota}')
        print(f'Menor nota: {menor_nota}')
        print(f'Aprovados: {quant_aprovados}')
        print(f'Recuperação: {quant_recuperacao}')
        print(f'Reprovados: {quant_reprovados}')
    except:
        print('Não foi inserido alunos')
            
            
def obter_maior(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2
    

def obter_menor(n1, n2):
    if n1 < n2:
        return n1
    else:
        return n2
    

main()