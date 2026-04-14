def troco():    
    valor_total = float(input("Digite o valor total: "))
    valor_pago = float(input("Digite o valor pago: "))

    if valor_pago < valor_total:
        print("Valor insuficiente!")
    else:
        troco = valor_pago - valor_total
        print("O troco é:", troco)

        notas100 = int(troco / 100)
        troco = troco % 100
        if notas100 > 0:
            print(notas100, "nota(s) de R$ 100")

        notas50 = int(troco / 50)
        troco = troco % 50
        if notas50 > 0:
            print(notas50, "nota(s) de R$ 50")

        notas20 = int(troco / 20)
        troco = troco % 20
        if notas20 > 0:
            print(notas20, "nota(s) de R$ 20")

        notas10 = int(troco / 10)
        troco = troco % 10
        if notas10 > 0:
            print(notas10, "nota(s) de R$ 10")

        notas5 = int(troco / 5)
        troco = troco % 5
        if notas5 > 0:
            print(notas5, "nota(s) de R$ 5")

        notas2 = int(troco / 2)
        troco = troco % 2
        if notas2 > 0:
            print(notas2, "nota(s) de R$ 2")

        moedas1 = int(troco / 1)
        troco = troco % 1
        if moedas1 > 0:
            print(moedas1, "moeda(s) de R$ 1")

        moedas50 = int(troco / 0.50)
        troco = troco % 0.50
        if moedas50 > 0:
            print(moedas50, "moeda(s) de R$ 0.50")

        moedas25 = int(troco / 0.25)
        troco = troco % 0.25
        if moedas25 > 0:
            print(moedas25, "moeda(s) de R$ 0.25")

        moedas10 = int(troco / 0.10)
        troco = troco % 0.10
        if moedas10 > 0:
            print(moedas10, "moeda(s) de R$ 0.10")

        moedas5 = int(troco / 0.05)
        troco = troco % 0.05
        if moedas5 > 0:
            print(moedas5, "moeda(s) de R$ 0.05")

        moedas1 = int(round(troco, 2) / 0.01)
        if moedas1 > 0:
            print(moedas1, "moeda(s) de R$ 0.01")
troco()