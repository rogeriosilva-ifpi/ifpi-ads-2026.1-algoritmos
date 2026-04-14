def main():
    n = int(input('Digite o limite inferior(N): '))
    m = int(input('Digite o limite superior(M): '))
    print(' ')
    buscar_multiplos3_somar(n, m)
    
def buscar_multiplos3_somar(n, m):
    soma = 0
    if n >= m:
        print('O limite inferior deve ser menor que o superior, execute de novo!')
    
    else:
        print('Números:')
        for i in range(n , m):
            
            if i % 2 != 0 and i % 3 == 0:
                soma += i
                print(i)
    if soma == 0:
        print('Nenhum dos números nesse intervalo satisfazem a condição!')
                
    print(' ')
    print('Soma:', soma)


main()   