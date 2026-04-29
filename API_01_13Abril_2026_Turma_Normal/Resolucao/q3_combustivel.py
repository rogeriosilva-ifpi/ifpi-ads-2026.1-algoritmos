from utils import obter_real_positivo


def main():
  distancia = obter_real_positivo('Distância(km): ')
  perc_estrada = obter_real_positivo('Percentual em Estrada (%): ')
  valor_litro = obter_real_positivo('Valor Litro(R$): ')

  dist_estrada = (distancia / 100) * perc_estrada
  dist_cidade = distancia - dist_estrada

  litros_estrada = dist_estrada / 12
  litros_cidade = dist_cidade / 8

  litros_total = litros_cidade + litros_estrada
  custo =  litros_total * valor_litro

  resultado = f'''
  **** Resultado ****
  Distância Total: {distancia}
  Km na Estrada: {dist_estrada:.1f} - {perc_estrada}% - (Litros: {litros_estrada:.1f})
  Km na Cidade: {dist_cidade:.1f} - {100-perc_estrada}% - (Litros: {litros_cidade:.1f})
  
  Litros: {litros_total:.1f}
  Custo da Viagem: R$ {custo:.2f}
  '''

  print(resultado)

main()