def main():
    n = int(input("digite um número inteiro: "))
    divisores, total = calcular(n)
    print("divisores: ", divisores)
    print("total: ", total)


def calcular(n):
    divisores= ""
    total= 0

    for i in range(1, n + 1):
        if n % i==0:
            divisores+= str(i) + " "
            total=1
    return divisores, total





main()