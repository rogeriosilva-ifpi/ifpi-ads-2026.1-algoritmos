def main():
  #  Entrada
  salario = float(input('Salário (R$): '))

  # Processamento
  percentual = obter_percentual(salario)
  aumento = salario * percentual / 100
  novo_salario = salario + aumento

  # Saída
  print(f'Salário antes: R$ {salario:.2f}')
  print(f'Percentual de aumento {percentual}%')
  print(f'Valor do aumento R$ {aumento:.2f}')
  print(f'Novo Salário R$ {novo_salario:.2f}')


def obter_percentual(salario):
  if salario <= 280:
    return 20
  elif salario <= 700:
    return 15
  elif salario <= 1500:
    return 10 
  else:
    return 5


main()