from utils import obter_inteiro_positivo


def main():
  # n = int(input('N:'))
  n = obter_inteiro_positivo('N: ')
  contador = 0

  print('Divisores: ', end='')
  for numero in range(1, n+1):
    if n % numero == 0:
      contador += 1
      print(numero, end=' ')
  
  print()
  print(f'Total: {contador}')

main()