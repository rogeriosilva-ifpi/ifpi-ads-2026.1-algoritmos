def main():
    n = int(input("Digite um número inteiro positivo:"))
    
    total = 0
    contador = 0
    divisor = 1

    while contador < n:
        
        if n % divisor == 0:
            print('Divisor:')
            print(divisor)
            total += 1
        
        contador += 1
        divisor += 1

    
    

    
    print(f"Total de divisors:{total}")










main()