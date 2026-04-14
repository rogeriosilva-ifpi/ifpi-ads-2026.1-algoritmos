def calcular_troco():
    total_compra = 0
    
    while True:
        print("\n1 - Lançar Preço")
        print("2 - Finalizar e Pagar")
        opcao = input("Escolha: ")
        
        if opcao == "1":
            preco = float(input("Preço do produto: R$ "))
            total_compra = total_compra + preco
        elif opcao == "2":
            break

    print(f"Total da compra: R$ {total_compra:.2f}")
    pago = float(input("Valor pago: R$ "))
    if pago < total_compra:
        print("Valor insuficiente!")
    else:
        troco = pago - total_compra
        print(f"Troco total: R$ {troco:.2f}")
        centavos = round(troco * 100)

        qtd = centavos // 10000
        if qtd > 0:
            print(f"{qtd} nota(s) de R$ 100,00")
            centavos = centavos % 10000
        qtd = centavos // 5000
        if qtd > 0:
            print(f"{qtd} nota(s) de R$ 50,00")
            centavos = centavos % 5000
        qtd = centavos // 2000
        if qtd > 0:
            print(f"{qtd} nota(s) de R$ 20,00")
            centavos = centavos % 2000
        qtd = centavos // 1000
        if qtd > 0:
            print(f"{qtd} nota(s) de R$ 10,00")
            centavos = centavos % 1000
        qtd = centavos // 500
        if qtd > 0:
            print(f"{qtd} nota(s) de R$ 5,00")
            centavos = centavos % 50
        qtd = centavos // 200
        if qtd > 0:
            print(f"{qtd} nota(s) de R$ 2,00")
            centavos = centavos % 200
        qtd = centavos // 100
        if qtd > 0:
            print(f"{qtd} moeda(s) de R$ 1,00")
            centavos = centavos % 100
        qtd = centavos // 50
        if qtd > 0:
            print(f"{qtd} moeda(s) de R$ 0,50")
            centavos = centavos % 50
        qtd = centavos // 25
        if qtd > 0:
            print(f"{qtd} moeda(s) de R$ 0,25")
            centavos = centavos % 25
        qtd = centavos // 10
        if qtd > 0:
            print(f"{qtd} moeda(s) de R$ 0,10")
            centavos = centavos % 10
        qtd = centavos // 5
        if qtd > 0:
            print(f"{qtd} moeda(s) de R$ 0,05")
            centavos = centavos % 5
        qtd = centavos // 1
        if qtd > 0:
            print(f"{qtd} moeda(s) de R$ 0,01")
            centavos = centavos % 1

calcular_troco()