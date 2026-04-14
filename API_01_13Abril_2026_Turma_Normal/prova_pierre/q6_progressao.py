def main():
    n1 = int(input('N1: '))
    qtd = int(input('Quantidade de termos:'))
    r = int(input('R: '))

    def pa(n, r, qtd):
        contador = 0
        sequencia = ''
        somatorio = 0

        while contador <= qtd:
            sequencia += str(n) + ' '
            somatorio += n
            n += r
            contador += 1
        media = somatorio / qtd
        return f'Sequência: {sequencia}\nSomatório: {somatorio}\nMédia: {media:.2f}'
    
    resultado = pa(n1, r, qtd)
    print(resultado)
    continuar = input('Continuar? (S/N): ')

    while continuar == 'S':
        n1 = int(input('N1: '))
        qtd = int(input('Quantidade de termos:'))
        r = int(input('R: '))

        resultado = pa(n1, r, qtd)
        print(resultado)
        continuar = input('Continuar? (S/N): ')



main()