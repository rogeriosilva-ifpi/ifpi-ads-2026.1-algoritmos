from utils import obter_int_positivo

def main():
    distancia = obter_int_positivo('Distância total (km): ')
    percent_estrada = float(input('Percentual em estrada (0-100): '))
    preco_litro = float(input('Preço do litro: '))

    percent_cidade = calcular_percent(percent_estrada)
    qtd_litros_estrada, qtd_litros_cidade, total_litros = qtd_litros(distancia, percent_estrada, percent_cidade)
    valor_total = calcular_valor(total_litros, preco_litro)

    icone = '=' * 50

    print(f'''{icone}
Consumo da estrada ----- {qtd_litros_estrada:.2f}L
Consumo da cidade ----- {qtd_litros_cidade:.2f}L
Total de litros necessários ----- {total_litros:.2f}L
Custo total da viajem ----- R${valor_total:.2f}
{icone}''')



def calcular_percent(percent_estrada):
    percent_cidade = 100 - percent_estrada
    return percent_cidade


def qtd_litros(distancia, percent_estrada, percent_cidade):
    distancia_estrada = distancia * (percent_estrada / 100)
    distancia_cidade = distancia * (percent_cidade / 100)
    qtd_litros_estrada = distancia_estrada / 12
    qtd_litros_cidade = distancia_cidade / 8
    total_litros = qtd_litros_estrada + qtd_litros_cidade
    return qtd_litros_estrada, qtd_litros_cidade, total_litros


def calcular_valor(total_litros, preco):
    valor_total = total_litros * preco
    return valor_total



if __name__ == "__main__":
    main()