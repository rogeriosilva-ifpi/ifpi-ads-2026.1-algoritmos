from utilitaros import inteiro

def main():
    while True:    
        a = inteiro('insira 1° termo: ')
        r = inteiro('insira a razão: ')
        n_termos = inteiro('insira o numero de termos: ')

        while n_termos < 2:
            print('quantidade de termos insuficiente (min 2)')
            n_termos = inteiro('insira o numero de termos: ')

        inicial = a
        soma_total = a
        media = soma_total / n_termos
        for i in range(n_termos-1):
            print(inicial)
            progressao = inicial + r
            soma_total += progressao
            inicial = progressao
        print(f'{inicial}\nsoma total: {soma_total}\nmedia: {media}')

        continuar = inteiro('você deseja fazer outra progressao? (s-1, n-0)')
        if continuar == 0:
            break
        else:
            continue


    


main()