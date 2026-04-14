def main():
    n = int(input('N: '))
    m = int(input('M: '))

    print('Números: ')
    somatorio = 0
    for i in range(n, m+1):
        if i % 2 != 0 and i % 3 == 0:
            print(i)
            somatorio += i
    if somatorio == 0:
        print(f'Os números do intervalo {n} - {m} não são ímpares e não são divisíveis por 3.')
    print(f'Soma: {somatorio}')
main()