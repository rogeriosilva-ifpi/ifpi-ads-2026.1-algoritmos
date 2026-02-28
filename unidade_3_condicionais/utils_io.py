def escrever(conteudo: str):
  print(conteudo)


def obter_texto(instrucoes = 'Digite algo: '):
  entrada = input(instrucoes)
  return entrada


def obter_inteiro(instrucoes = 'Digite um inteiro: '):
  numero = int(input(instrucoes))
  return numero


def obter_numero_real(instrucoes = 'Digite um real: '):
  numero = float(input(instrucoes))
  return numero