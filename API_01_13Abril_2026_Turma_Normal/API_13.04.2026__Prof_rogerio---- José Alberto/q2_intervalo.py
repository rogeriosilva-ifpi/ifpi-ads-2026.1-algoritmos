def main():

    numero_inferior = int(input('Digite o menor número: '))

    numero_superior = int(input('Digite o maior número: '))


    soma = 0





    for n in range(numero_inferior, numero_superior + 1):

        if n % 2 != 0 :

            if n % 3 == 0:

                soma += n

                print(n)
                print()
    
    print(f'Soma: {soma}')


























main()