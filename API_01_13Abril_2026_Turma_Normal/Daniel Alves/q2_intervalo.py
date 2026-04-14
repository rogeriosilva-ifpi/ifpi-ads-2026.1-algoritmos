def main():

    N = int(input('Digite um numero inteiro N:  '))
    M = int(input('Digite um numero inteiro M maior que N:  '))
    
    
    numeros = [i for i in range(N, M + 1) if i%2 != 0 and i%3 == 0]
    
    print(numeros)
        
main()