def main():
    soma = 0

    divisor = 0




    while True:

        primeiro_termo = int(input('Digite o primeiro termo: '))
        print()
        razao = int(input('Digite a razão: '))
        print()
        n_termos = int(input('Digíte o ultimo termo: '))
        print()


        for n in range(primeiro_termo, n_termos +  1, razao):

            divisor += 1

            soma += n

            print(n)


        media = soma / divisor

        print()
        print(f'média: {media}')
        print(f'Soma total: {soma}')


        continuar = input('Deseja continuar(sim ou não)? ')

        if continuar == 'nao' or continuar == 'não':
            break



            





























main()