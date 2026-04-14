def main():
    n = int(input("Digite um número inteiro como o início:"))
    m = int(input("Digite um número inteiro como o fim:"))
    soma = 0

    for i in range(n, m + 1):
        if i % 2 != 0:
            if i % 3 == 0:
                print(i)
                soma += i

    print(f"A soma dos números divisíveis por 3, entre {n} e {m}, é igual a {soma}")



















main()