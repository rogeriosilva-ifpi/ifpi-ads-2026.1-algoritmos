def main():
    n = int(input('Número: '))

    def lista_divisores(n):
        lista = ''
        divisor = 1
        while divisor <= n:
            if n % divisor == 0:
                lista += str(divisor) + ' '
            divisor += 1
        return lista
    
    def calcular_total(n):
        divisor = 1
        somatorio = 0
        while divisor <= n:
            if n % divisor == 0:
                somatorio += 1
            divisor += 1
        return somatorio



    divisores = lista_divisores(n)
    total_divisores = calcular_total(n)

    print(f'Divisores: {divisores}')
    print(f'Total de divisores {total_divisores}.')

main()