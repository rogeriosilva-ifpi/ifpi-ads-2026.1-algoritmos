def main():
    distancia = float(input('Digite a distância em KM:  '))
    estrada = float(input('A % percorrida em estrada:  '))
    cidade = float(input('A % percorrida na cidade:  '))
    preco = float(input('R$ da gasolina:  '))

    dist_estrada = distancia*estrada/100
    dist_cidade = distancia*cidade/100

    con_estrada = dist_estrada/12
    con_cidade = dist_cidade/8

    consumo_total = con_estrada+con_cidade
    preco_total= preco*consumo_total

    print(f'No tracho da cidade o consumo foi de {con_cidade:.2f}L na estrada doi {con_estrada:.2f}L.')
    print(f'No toltal {consumo_total:.2f}L.')
    print(f'E foi gasto R${preco_total:.2f}.')

    








main()