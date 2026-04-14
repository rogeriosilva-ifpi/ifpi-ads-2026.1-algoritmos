def main():
    numero = int(input('Informe o número: '))
    total = 1

    for i in range(1, numero):
        if numero % i == 0:
            print(f'Divisor: {i}')
            total += 1
    print(f'Total: {total} divisores')


        


main()