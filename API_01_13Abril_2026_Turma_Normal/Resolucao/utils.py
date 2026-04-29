def obter_inteiro(prompt: str):
  while True:
    try:
      numero = int(input(prompt))
      return numero
    except:
      print('Número inválido')


def obter_inteiro_positivo(prompt: str):
  numero = obter_inteiro(prompt)

  while not numero > 0:
    print('Favor digitar um número positivo!')
    numero = obter_inteiro(prompt)
  
  return numero


def obter_inteiro_minimo(prompt: str, minimo: int):
  numero = obter_inteiro(prompt)

  while not numero >= minimo:
    print(f'Favor no mínimo {minimo}.')
    numero = obter_inteiro(prompt)
  
  return numero


def obter_inteiro_faixa(prompt: str, minino: int, maximo: int):
  numero = obter_inteiro(prompt)

  while not (numero >= minino and numero <= maximo):
    print(f'Favor digitar um número de {minino} até {maximo}!')
    numero = obter_inteiro(prompt)
  
  return numero


def obter_real(prompt: str):
  while True:
    try:
      numero = float(input(prompt))
      return numero
    except:
      print('Número real inválido.')


def obter_real_positivo(prompt: str):
  numero = obter_real(prompt)

  while not numero > 0:
    print('Favor digitar um número real positivo!')
    numero = obter_real(prompt)
  
  return numero


def obter_real_faixa(prompt: str, minino: float, maximo: float):
  numero = obter_real(prompt)

  while not (numero >= minino and numero <= maximo):
    print(f'Favor digitar um número de {minino} até {maximo}!')
    numero = obter_real(prompt)
  
  return numero


def obter_real_minimo(prompt: str, minimo: float):
  numero = obter_real(prompt)

  while not numero >= minimo:
    print(f'Favor no mínimo {minimo:.2f}.')
    numero = obter_real(prompt)
  
  return numero