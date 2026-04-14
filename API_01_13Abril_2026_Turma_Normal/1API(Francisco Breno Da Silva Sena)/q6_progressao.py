def main():
    pergunta = input("Deseja fazer uma PA? ( s - sim ou n - não)")

    while pergunta == 's':
        a = int(input("Digite o primeiro termo da PA:"))
        r = int(input("Digite a razão da PA:"))
        n = int(input("Digite a qunatidade de termos da PA:"))
        soma = 0
        quant = 0

        for i in range(a, n + 1, r):
            print(i)
            soma += i
            quant += 1

        media = soma / quant
        print(f"A soma total dos termos da PA é: {soma}")
        print(f"A média dos termos é: {media}")

        pergunta = input("Deseja fazer uma outra PA? ( s - sim ou n - não)")







main()