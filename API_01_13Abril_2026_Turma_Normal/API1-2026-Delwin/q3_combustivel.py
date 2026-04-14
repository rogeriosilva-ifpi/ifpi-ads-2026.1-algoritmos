from utils import obterInteiro, obterPorcentagem, obterFloat

def Main():
    #Chamando obterInteiro para pedir número 
    distancia = obterInteiro('Informe a distância (km): ')
    #Chamando obterFloat para pedir número 
    preco = obterFloat('Informe o preço por litro (R$): ')

    #Calculando porcentagems do trajeto e distâncias
    porcentagem_estrada = obterPorcentagem('Quantos % do trajeto é estrada? ')
    porcentagem_cidade = 1 - porcentagem_estrada
    distancia_estrada = distancia * porcentagem_estrada
    distancia_cidade = distancia * porcentagem_cidade

    #Calculando consumos
    consumo_cidade = calculaConsumo(8, distancia_cidade)
    consumo_estrada = calculaConsumo(12, distancia_estrada)

    #Exibindo resultados
    print(f'Consumo na cidade: {consumo_cidade:.2f}')
    print(f'Consumo na estrada: {consumo_estrada:.2f}')
    print(f'Consumo total: {consumo_cidade + consumo_estrada:.2f}')
    print(f'Custo total: R${(consumo_cidade + consumo_estrada) * preco:.2f}')



def calculaConsumo(consumo, uso):
    #Recebe um valor de consumo por unidade e um uso, retornando a unidade
    return uso/consumo


Main()