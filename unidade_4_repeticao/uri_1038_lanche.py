def main():
  entrada = input()
  dados = entrada.split()
  codigo = int(dados[0])
  qtd = int(dados[1])

  total = calcular_valor_item(codigo, qtd)

  print(f'Total: R$ {total:.2f}')


def calcular_valor_item(codigo, qtd):
  if codigo == 1:
    return qtd * 4.00
  elif codigo == 2:
    return qtd * 4.50
  elif codigo == 3:
    return qtd * 5.00
  elif codigo == 4:
    return qtd * 2.00
  else:
    return qtd * 1.50


main()