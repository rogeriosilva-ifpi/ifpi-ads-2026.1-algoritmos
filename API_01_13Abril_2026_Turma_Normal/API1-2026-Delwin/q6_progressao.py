from utils import obterInteiro, confirma

def Main():
    #Chamando obterInteiro para pedir números
    a = obterInteiro('Digite o primeiro termo: ')
    r = obterInteiro('Digite a razão: ')
    n = obterInteiro('Digite o número de termos (pelo menos 2): ')

    while True:
        exibeProgressao(a, r, n)
        if confirma('Deseja continuar? (S/N)') == False:
            break


def exibeProgressao(a, r, n):
    #Recebe o primeiro elemento (a), a razão(r) e o número de elementos(n) de uma pa e exiba os termos, a soma destes e a média dos elementos
    print('Termos da PA: ')
    print(a, end=' ')
    
    soma = a
    for i in range (n-1):
        a += r
        soma += a
        print(a, end=' ')

    print(f'Soma dos termos: {soma}')
    print(f'Média dos termos: {soma/n}')



Main()