def main():

    n = int(input('Digite um número inteiro: '))
    
    if n <= 0:
        print('Núemro maior quq zero')
        return
    
    divisores = []


    for i in range(1, n + 1): 
        if n % 1 == 0:
            divisores.append(1)
            


      
        print(f'Divisores: {divisores} ')
        print(f'Total: {len(divisores)}')


      

    

main()