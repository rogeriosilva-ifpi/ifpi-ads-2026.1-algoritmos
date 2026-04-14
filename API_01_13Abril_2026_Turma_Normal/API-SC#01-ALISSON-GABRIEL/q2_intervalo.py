def main():
    n = int(input('Informe N: '))
    m = int(input('Informe M: '))

    somatorio = 0
    for i in range (n, m):
        if i % 2 != 0 and i % 3 == 0:
            print(f'{i} é um divisor de 3 e ímpar')
            somatorio += i

    print(f'Soma: {somatorio}')


main()