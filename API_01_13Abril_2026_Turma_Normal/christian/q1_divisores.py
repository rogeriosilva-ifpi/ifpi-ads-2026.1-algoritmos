from utils_io import limpar_tela

def main():
    limpar_tela()
    
    n = int(input('Valor de N: '))
    contador=0
    print('Divisores:')
    for i in range(1,n+1):
        if n%i==0:
            print(i, end=' ')
            contador+=1
    print(f'\nQuantidade de divisores: {contador}')

main()