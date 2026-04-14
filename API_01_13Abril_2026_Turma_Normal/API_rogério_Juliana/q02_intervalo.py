from utilitaros import inteiro

def main():
    n = inteiro('digite um valor para N:')
    m = inteiro('digite um valor para M:')
    soma = 0
    for i in range(n,m+1):
        impar = impares(i)
        div_3 = divisivel3(i)
        if impar and div_3:
            print(i, end=' ')
            soma += i

    if soma > 0:
        print(f'\n{soma}')
    else:
        print('nenhum dos numeros desse ntervalo atende às regras')
        
'''def validador(m,n):
    while True:
        if n >= m:
            print('M deve ser maior que N, tente novamente')
            n = int(input('digite o valor de N: '))'''
            
def impares(i):
    if i % 2 != 0:
        return i
        
def divisivel3(i):
    if i % 3 == 0:
        return i
    


    
main()