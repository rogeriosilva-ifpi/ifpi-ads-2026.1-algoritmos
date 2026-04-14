def main():
    a = int(input('Primeiro Termo: '))
    r = int(input('Razão: '))
    n = int(input('Número de termos: '))
    
    termo = a
    soma = 0
    for i in range(n):
        print(termo)
        termo += r
        soma += termo
    
    media = soma / n
    print(f'Soma total: {soma}')
    print(f'Media dos termos: {media:.2f}')

    print('Deseja calcular outra prrogressão?')
    opcao = int(input('1 - sim  2 - não'))

    while opcao == 1:
        termo = a
        soma = 0
        for i in range(n):
            print(termo)
            termo += r
            soma += termo
    
        media = soma / n
        print(f'Soma total: {soma}')
        print(f'Media dos termos: {media:.2f}')

        print('Deseja calcular outra prrogressão?')
        opcao = int(input('1 - sim  2 - não'))
        if opcao == 2:
            break
main()