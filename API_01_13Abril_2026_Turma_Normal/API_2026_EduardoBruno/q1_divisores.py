def main():
    try:
        n = int(input('Digite um número inteiro positivo: '))
        if n >= 0:
            soma_divisores = 0
            print('Divisores: ',end='')
            for i in range(1, n+1):
                if n % i == 0:
                    print(f'{i}',end= ' ')
                    soma_divisores += 1
            print(f'\nTotal: {soma_divisores} divisores')
        else:
            print('Digite um valor válido!')
    except ValueError:
        print('Digite um valor válido!')








main()