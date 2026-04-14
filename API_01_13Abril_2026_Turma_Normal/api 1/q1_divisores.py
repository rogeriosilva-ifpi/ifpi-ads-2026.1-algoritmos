def main():
    N = int(input('Escreva um número inteiro positivo:'))


    divisores(N)


def divisores(N):
    if N < 1:
        print('O numero deve ser positivo.')
    else:
        print('Os divisores são:')
        for i in range(1, N+1):
            if N%i == 0:
              print(i, end=" ")
    
    
main()