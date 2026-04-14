def main():
    
    N = int(input("Digite um número: "))
    divisores = 0

    for i in range(N+1):
        if N % i == 0:

            divisores += 1
            print(f"Divisores: {i}")
            print(f"Total: {divisores} divisores")




main()