def main():
    
    distancia = int(input("Distancia: "))
    trecho = int(input("Porcentagem em estrada: "))
    preco = int(input("Preço combustível: "))
    

    trecho_estrada = (distancia * (trecho/100))
    trecho_cidade = (distancia - trecho_estrada)
    gasto_estrada = (trecho_estrada / 12)
    gasto_cidade = trecho_cidade / 8
    gasto_total = gasto_cidade + gasto_estrada
    preco_total = preco * gasto_total

    print("\no consumo na estrada foi de: %.2f"%(gasto_estrada), "litros")
    print("\no consumo na cidade foi de: %.2f"%(gasto_cidade), "litros")
    print("\no total de litros necessários são: %.2f"%(gasto_total), "litros")
    print("\no custo total da viagem é de: %.2f"%(preco_total), "R$")




main()