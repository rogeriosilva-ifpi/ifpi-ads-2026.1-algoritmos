def main():
    a = int(input('Informe o primeiro termo: '))
    r = int(input('Informe a razão: '))
    n_termos = int(input('Informe a quantia de termos: '))

    soma = 0

    for i in range(a, n_termos+1, r):
        print(i)
        soma += i
    
    media = soma / n_termos

    resultado = f'''
Soma total: {soma}
Média: {media:.2f}'''
    print(resultado)

    continuar = input('Quer continuar?(S/N) ')
    while continuar == 'S':
        a = int(input('Informe o primeiro termo: '))
        r = int(input('Informe a razão: '))
        n_termos = int(input('Informe a quantia de termos: '))

        soma = 0
        media = 0

        for i in range(a, n_termos+1, r):
            print(i)
            soma += i
    
        media = soma / n_termos

        resultado = f'''
        Soma total: {soma}
        Média: {media:.2f}'''
        print(resultado)

        continuar = input('Quer continuar?(S/N) ')


main()