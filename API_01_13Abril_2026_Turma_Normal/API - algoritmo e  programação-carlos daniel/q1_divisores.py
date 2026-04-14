def calcular_divisores():
    n = int(input("Digite um número inteiro positivo: "))
    
    if n <= 0:
        print("Erro: O número deve ser positivo!")
    else:
        contador = 0
        print(f"Divisores de {n}:", end=" ")
        
        for i in range(1, n + 1):
            if n % i == 0:
                print(i, end=" ")
                contador = contador + 1
        
        print(f"\nTotal: {contador} divisores")

calcular_divisores()