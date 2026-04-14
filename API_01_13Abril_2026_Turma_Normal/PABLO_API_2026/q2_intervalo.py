from utils import *

def main():
    n = obter_inteiro()
    m = obter_inteiro()
    
    divs, somatorio = obter_intervalo(n, m)
            
    if divs == '':
        print('Oh não há números que satisfaçam a condição')
    else:
        print(f'Números: {divs}')
        print(f'Soma: {somatorio}')
    
    
def obter_intervalo(n, m):
    divs = ''
    somatorio = 0
    
    for i in range(n, m):
        if i % 2 != 0 and i % 3 == 0:
            divs += ' ' + str(i)
            somatorio += i
            
    return divs, somatorio


main()