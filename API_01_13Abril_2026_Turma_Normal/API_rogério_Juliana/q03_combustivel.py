from utilitaros import positivo

def main():
    distancia_total = positivo('distancia total (km): ')
    percentual_estrada = positivo('quantos porcento do percurso é na estrada? ')
    preco_litro = positivo('preço litro: ')
    preco_total = calculo(distancia_total,percentual_estrada,preco_litro)

    print(f'distancia total: {distancia_total}km \
          percentual_estrada = {percentual_estrada}%\
          preco litro = R${preco_litro}\
          ---------gastos totais------------\
          preco total = R${preco_total}')
          
def calculo(dt,pe,pl):
    estrada = dt * (pe / 100)
    cidade = dt - estrada

    preco_estrada = estrada * pl
    preco_cidade = cidade * pl
    preco_total = preco_cidade + preco_estrada

    return preco_total



main()