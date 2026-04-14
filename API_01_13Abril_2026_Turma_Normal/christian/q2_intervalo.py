from utils_io import limpar_tela

def main():
    limpar_tela() 

    n = int(input('Insira o valor de N: '))
    m = int(input('Insira o valor de M: '))
    while m<n:
        m = int(input('O valor de M precisa ser MAIOR que N: '))
    soma=0
    print('Divisores: ')
    for i in range(n,m):
        if numero_impar(i)==True and divisivel_por_tres(i)==True:
            print(i, end=' ')
            soma+=i
    print(f'\nSoma: {soma}')
    
def numero_impar(n):
    if n%2!=0:
        return True 
    else: 
        return False
    
def divisivel_por_tres(m):
    if m%3==0:
        return True 
    else:
        return False

main()
