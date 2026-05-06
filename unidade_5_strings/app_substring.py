
from io_utils import obter_inteiro_faixa


def main():
  texto = input('Texto: ')

  inicio = obter_inteiro_faixa('Início: ', 0, len(texto)-1)
  final = obter_inteiro_faixa('Final: ', inicio, len(texto)-1)

  fatia = substring(texto, inicio, final)

  print(fatia)


def substring(texto, inicio, final):
  novo_texto = ''
  for i in range(inicio, final+1):
    novo_texto = novo_texto + texto[i]
  
  return novo_texto


main()