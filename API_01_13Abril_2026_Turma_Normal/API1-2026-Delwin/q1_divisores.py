from utils import obterInteiro

def Main():
    #Chamando obter inteiro para pedir número 
    n = obterInteiro('Digite o número: ')
    
    #Contando e mostrando divisores
    print('Divisores: ', end=' ')
    soma = 0
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=' ')
            soma += 1
    print(f'Total: {soma}')


Main()