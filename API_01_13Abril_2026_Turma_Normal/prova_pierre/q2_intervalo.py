def main():

    n = int(input('N: '))
    m = int(input('M: '))

    while n > m:
        print('O número M prescisa ser maior que N')
        n = int(input('N: '))
        m = int(input('M: '))

    def condicao(n, m):
        somatorio = 0
        lista = ''
        for i in range (n, m+1):
            if (i % 2 != 0) and (i % 3 == 0):
                lista += str(i) + ' '
                somatorio += i
        if somatorio == 0:
            return f'Nenhum número entre {n} e {m} satisfaz a condição.'
        else:
            return f'Números: {lista}\nSoma: {somatorio}'

    print(condicao(n, m))


main()