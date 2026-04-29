def main():
    distancia = int(input('Distancia total em Km:'))
    percentual = int(input('Percentual em estrada(0-100%):'))
    valor = float(input('Preço do combustível:'))

    gasto(distancia, percentual, valor)
    
def gasto(distancia, percentual, valor):
    estrada = distancia*(percentual/100)
    consumo_estrada = 12/valor
    consumo_cidade = 8/valor
    custo_estrada = consumo_estrada*estrada
    custo_cidade = (distancia-estrada)*consumo_cidade
    custo_total = (custo_estrada+custo_cidade)*valor
    print(f'Consumo na estrada:{custo_estrada}')
    print(f'Consumo na cidade:{custo_cidade}')
    print(f'total de litros necessários:{custo_total}')


    
    
main()