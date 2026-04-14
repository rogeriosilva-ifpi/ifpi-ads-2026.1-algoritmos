import os
from utils.os_utils import limpar_tela
from utils.number_utils import obter_inteiro, obter_float


def obter_distancia():
    print("Insira a distância total (km): ", end="")
    try:    
        distancia = obter_inteiro()
    except:
        print("Insira um número inteiro para a distância: ", end="")
        distancia = obter_inteiro()
    return distancia


def obter_percentual_estrada():
    print("Insira quantos porcento (%) da viagem será feita em estrada: ", end="")
    try:
        estrada = obter_inteiro()
    except:
        print("Insira um número inteiro para o percentual da viagem que será feita em estrada: ", end="")
        estrada = obter_inteiro()
    return estrada


def obter_preco_combustivel():
    print("Insira o preço do combustível (R$): ", end="")
    try:
        preco_combustivel = obter_float()
    except:
        print("Insira um número decimal ou inteiro para definir o valor do combustível (R$): ", end="")
        preco_combustivel = obter_float()
    return preco_combustivel


def calcular_consumo(distancia, estrada):
    total_estrada = distancia * (estrada / 100)
    total_cidade = distancia - total_estrada
    consumo_estrada = 12 * total_estrada
    consumo_cidade = 8 * total_cidade
    return consumo_estrada, consumo_cidade


def calcular_litros(consumo_cidade, consumo_estrada):
    consumo_litros = consumo_cidade + consumo_estrada
    return consumo_litros


def calcular_custo(consumo_litros, preco_combustivel):
    custo_total = consumo_litros * preco_combustivel
    return custo_total


def printar_valores(consumo_estrada, consumo_cidade, consumo_litros, custo_total):
    print(f"""
    Consumo na estrada: {consumo_estrada}
    Consumo na cidade: {consumo_cidade}
    Consumo total de litros: {consumo_litros}
    Custo total (R$): {custo_total}
    """)


def main():
    limpar_tela()
    distancia = obter_distancia()
    estrada = obter_percentual_estrada()
    preco_combustivel = obter_preco_combustivel()
    consumo_estrada, consumo_cidade = calcular_consumo(distancia, estrada)
    consumo_litros = calcular_litros(consumo_cidade, consumo_estrada)
    custo_total = calcular_custo(consumo_litros, preco_combustivel)
    printar_valores(consumo_estrada, consumo_cidade, consumo_litros, custo_total)


main()