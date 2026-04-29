def main():
    N = int(input('Escreva um número inteiro:'))
    M = int(input('Escreva um número inteiro maior que N:'))
    if M <= N:
        print('M deve ser maior que N')
        M = int(input('Escreva um número inteiro maior que N:'))

    print('Numeros:')
    div_impares(N, M)


def div_impares(N, M):
    soma = 0
    for i in range(N, M+1):
        if i%2 != 0 and i%3 == 0:
            numeros = i
            soma = soma+i
            print(numeros, end=" ")
    print(f'\nSoma:{soma}')
        
        

main()