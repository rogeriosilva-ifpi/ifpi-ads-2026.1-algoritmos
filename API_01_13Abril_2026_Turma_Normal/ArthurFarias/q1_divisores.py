def main():
    numero = int(input("\nDigite um número inteiro positivo: "))
    
    while numero <= 0:
        numero = int(input("Este número não é um inteiro positivo. Digite um novo número: "))
      
    quant_divisores = 0

    for i in range(1, numero+1):
        if numero % i == 0:
            print(i,end=" ")
            quant_divisores = quant_divisores + 1
    
    print(f"\n{quant_divisores} divisores.")


main()