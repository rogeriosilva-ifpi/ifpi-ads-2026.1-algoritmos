def main():
  distancia = float(input('Distância (km): '))
  perc_estrada = float(input('Perc. Estrada(%): '))
  valor_litro = float(input('Preço Litro(R$): '))

  estrada_km = (distancia / 100) * perc_estrada
  cidade_km = distancia - estrada_km

  estrada_litros = estrada_km / 12
  cidade_litros = cidade_km / 8

  litros_total = estrada_litros + cidade_litros
  custo = litros_total * valor_litro

  print(f'Litros Estrada: {estrada_litros:.1f} ({estrada_km}km)')
  print(f'Litros Cidade: {cidade_litros:.1f} ({cidade_km}km)')
  print(f'Total Litros: {litros_total:.1f}')
  print(f'Custo viagem: {custo:.2f}')


main()