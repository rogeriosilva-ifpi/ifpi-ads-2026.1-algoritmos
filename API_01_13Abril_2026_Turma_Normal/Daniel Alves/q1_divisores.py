def main():


    while True:
        try:
            n = int(input('Digite um numero inteiro:  '))
            divisores = [i for i in range(1, n + 1) if n%i==0]
            tamanho = len(divisores)

            print(f'Divisores= {divisores}')
            print(f'Total: {tamanho} divisores.')

        except ValueError:
            print('Erro: Digite um numero inteiro.')

main()