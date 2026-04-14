def main():
   calcular_consumo()
   
def calcular_consumo():
   distan_total = int(input('Informe a distância total do trajeto(KM): '))
   percen_estrada = int(input('Informe o percentual em estrada do trajeto(%): '))
   preco_litro =  float(input('Informe o preço do litro do combustível(R$): '))
   
   trajeto_estrada = distan_total * (percen_estrada/100) 
   trajeto_cidade = distan_total - trajeto_estrada
   
   litros_estrada = trajeto_estrada / 12
   litros_cidade = trajeto_cidade / 8
   litros_totais = litros_estrada + litros_cidade
   
   consumo = litros_totais * preco_litro
   print(f'O consumo da viagem é {consumo} R$')

main()