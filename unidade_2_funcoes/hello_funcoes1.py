def calcular_porcentagem(valor, percentual):
  resultado = valor * percentual/100
  return resultado


def obter_numero_real(descricao):
  valor = float(input(descricao))
  return valor

def escrever(conteudo):
  print(conteudo)


# Programa
total = obter_numero_real('Valor R$: ')
percentual = obter_numero_real('Percentual %: ')

r = calcular_porcentagem(total, percentual)

saida = f'> {percentual}% de R$ {total} é R$ {r}'

escrever(saida)