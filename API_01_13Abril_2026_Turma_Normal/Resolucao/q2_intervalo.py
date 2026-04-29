from utils import obter_inteiro_minimo, obter_inteiro_positivo


def main():
  n = obter_inteiro_positivo('N: ')
  m = obter_inteiro_minimo('M: ', n+1)
  soma = 0

  print('Divisores: ', end='')
  for numero in range(n, m+1):
    if numero % 2 != 0 and numero % 3 == 0:
      soma += numero
      print(numero, end=' ')
  
  print()
  print(f'Soma: {soma}')

main()