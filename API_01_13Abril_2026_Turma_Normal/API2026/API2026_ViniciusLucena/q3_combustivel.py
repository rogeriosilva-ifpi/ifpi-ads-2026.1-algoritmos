def main():
    distancia= float(input("digite a distancia: "))
    percentual= float(input("digite qual o percentual: "))
    preco= float(input("digite qual o preço: "))

    le, lc, total, custo = calcular(distancia, percentual, preco)
    mostrar(le, lc, total, custo)

#obs professor, Rogério: le significa litros na estrada// lc significa na cidade#

def calcular(d, p, preco):
    km_estrada = d * p / 100
    km_cidade = d - km_estrada

    litros_estrada = km_estrada / 12
    litros_cidade = km_cidade / 8

    total_litros = litros_estrada + litros_cidade
    custo_total = litros_estrada * preco

    return litros_estrada, litros_cidade, total_litros, custo_total


def mostrar(le, lc, total, custo):
    print ("custo na estrada: ", le)
    print ("custo na cidade: ", lc)
    print ("total: ", total,"KM")
    print ("o custo foi:R$", custo)




main()