from utils import obterInteiro

def Main():
    #Chamando obter inteiro para pedir números 
    n = obterInteiro('Digite o limite inferior: ')
    m = obterInteiro('Digite o limite superior: ')

    #Variável para guardar soma
    soma = 0
    
    #Imprimindo números ímpares divisíveis por 3
    print('Divisores: ', end=' ')
    for i in range(n, m+1):
        if i % 2 != 0 and i % 3 == 0:
            print(i, end=' ')
            soma += i
    
    #Imprimindo a soma dos números
    print(f'Soma: {soma}')

def obterInteiro(label):
    #Recebe uma string como parâmetro e retorna um número inteiro.
    while True:
        try:
            return int(input(label))
            break
        except:
            print('Valor inválido!')


Main()