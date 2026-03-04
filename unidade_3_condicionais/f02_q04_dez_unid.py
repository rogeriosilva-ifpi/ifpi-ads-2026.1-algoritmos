def main():
  numero = int(input('Número: '))

  dezena = obter_dezenas(numero)
  unidade = obter_unidades(numero)

  if dezena == unidade:
    print('Unidades e Dezenas são iguais!')
  else:
    print('Unidade e Dezenas NÃO são iguais.')


def obter_dezenas(numero):
  return numero // 10


def obter_unidades(numero):
  return numero % 10

main()