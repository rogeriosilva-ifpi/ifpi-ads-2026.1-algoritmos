def main():
    n = int(input("digite um número: "))
    m = int(input("digite um número: "))

    numeros, soma = calcular(n, m)

    print("números: ", numeros)
    print("a soma é: ", soma)


def calcular(n, m):
    numeros = ""
    soma = 0

    for i in range (n, m + 1):
        if i % 2 !=0 and i % 3 == 0:
            numeros += str (i) + " "
            soma += i
    return numeros, soma



main()