def intervalo(n, m):

    soma = 0
    contador = 0
    if n < m:
        print("Números: ")
        for i in range(n, m):
            restoimpar = i % 2
            resto3 = i % 3
            if restoimpar == 1 and resto3 == 0:
                print(i)
                soma +=i
                contador +=1
    else:
        print("'M' deve ser maior que 'N'")
    if contador == 0:
        print("Sem números elegíveis")

    return f"A soma é: {soma}"


def main():

    n = int(input(""))
    m = int(input(""))
    res = intervalo(n, m)
    print(res)
if __name__ == "__main__":
    main()
