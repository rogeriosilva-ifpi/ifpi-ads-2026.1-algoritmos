def main():
    distancia_total = int(input('Distãncia total(Km): '))
    percentual = int(input('Percentual em estrada: '))
    preco_litro = float(input('Preço do litro de combustível(R$): '))

    custo_total = distancia_total * preco_litro
    consumo_trecho = distancia_total * (percentual/100)
    total_litros = custo_total // preco_litro

    tela = f'''
    Consumo: {consumo_trecho}
    Litros necessários: {total_litros}
    Custo total: {custo_total}
'''
    print(tela)
main()