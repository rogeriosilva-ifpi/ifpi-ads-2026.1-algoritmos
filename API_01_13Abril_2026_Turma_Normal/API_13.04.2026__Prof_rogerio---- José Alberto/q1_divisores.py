def main():

    print('***Divisores***')

    print()

    numero = int(input('Digite o número: '))

    contador = 0



    for n in range(1, numero + 1):

        if numero % n == 0:

            contador += 1

            print(f'Divisor: {n}')
            print()

    print(f'Total de divisores: {contador}')


































main()