def main():
    n = int(input('N: '))

    print('Divisores: ')
    somatorio = 0
    for i in range(1, n+1):
        if n % i == 0:
            print(i)
            somatorio +=1
    print(f'Total de divisores: {somatorio} divisores.')


main()