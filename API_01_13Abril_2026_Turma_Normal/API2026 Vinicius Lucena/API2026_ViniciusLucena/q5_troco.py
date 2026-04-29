def main():
    total= float(input("digite o valor total:R$ "))
    pago= float(input("digite o valor pago:R$ "))

    if pago < total:
        print("saldo insuficiente para pagar a conta")
    else:
        troco = (pago-total) * 100
        calcular(int(troco))


def calcular(troco):
    notas = (100, 50, 20, 10, 5, 2, 1)

    for n in notas:
        qtd = troco // n

        if qtd > 0: 
            print(n/100, "notas de:", int(qtd))
            troco -= qtd*n




main()