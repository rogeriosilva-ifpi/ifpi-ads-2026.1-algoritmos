def main():
    numero_n = int(input("\nDigite um número inteiro: "))
    numero_m = int(input("Digite um numero inteiro, maior que o anterior: "))
    soma = 0

    while numero_n > numero_m:
        numero_m = int(input("O segungo número precisa ser maior que o primeiro. Digite um novo número: "))

    for i in range(numero_n,numero_m):
        if i % 2 != 0 and i % 3 == 0:
            print(i, end=" ")
            soma = soma + i
    
    print("\n",soma,sep="")


main()