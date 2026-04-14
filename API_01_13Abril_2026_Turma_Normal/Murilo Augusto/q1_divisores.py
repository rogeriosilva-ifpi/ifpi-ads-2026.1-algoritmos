def main():
    n = int(input("Entrada: "))
    
    for i in range(n):
        n = n/2
        resto = n % 2

    print(n)
    print(resto)

main()