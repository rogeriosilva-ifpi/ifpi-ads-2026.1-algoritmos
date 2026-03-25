def obter_inteiro(label: str):
  while True:
    try:
      numero = int(input(label))
      return numero
    except:
      print('Valor inválido! Digite um número inteiro')


def obter_inteiro_min(label: str, minimo: int):
  numero = obter_inteiro(label)

  while numero < minimo:
    print(f'O valor inválido! Digite pelo menos {minimo}')
    numero = obter_inteiro(label)

  return numero


def obter_inteiro_positivo(label: str):
  return obter_inteiro_min(label, 1)
