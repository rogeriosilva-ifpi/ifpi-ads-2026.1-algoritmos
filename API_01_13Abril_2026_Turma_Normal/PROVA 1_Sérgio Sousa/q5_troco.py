total = 0

while True:
    preco = float(input("Preco: R$ "))
    if preco == 0:
        break
    total += preco

pago = float(input("Valor pago: R$ "))
troco = pago - total

if troco < 0:
    print("Erro: Valor insuficiente!")
elif troco == 0:
    print("Pagamento exato!")
else:
    print(f"Troco: R$ {troco:.2f}")
    
    moedas = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
    textos = ["nota de 100", "nota de 50", "nota de 20", "nota de 10", 
              "nota de 5", "nota de 2", "nota de 1", "moeda de 0.50",
              "moeda de 0.25", "moeda de 0.10", "moeda de 0.05", "moeda de 0.01"]
    
    troco = round(troco, 2)
    
    for i in range(len(moedas)):
        qtd = int(troco / moedas[i])
        if qtd > 0:
            s = "s" if qtd > 1 else ""
            print(f"{qtd} {textos[i]}{s}")
            troco = round(troco - qtd * moedas[i], 2)



