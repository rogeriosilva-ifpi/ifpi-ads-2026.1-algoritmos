def main():
    inteiro = int(input('Digite um inteiro positivo: '))
    print(' ')
    mostrar_divisores(inteiro)

def mostrar_divisores(n):
    divisores = 0
    print('Divisores:')
    
    for i in range(1, n + 1):
        if n % i == 0:
            divisores += 1 
            print(i)    
    if i == n:
        print(' ')
        print(f'Total: {divisores} divisores')
                
                
main()         