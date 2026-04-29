def main():
  n = int(input('N: '))
  contador = 0

  print('Divisores', end=' ')
  for i in range(1, n+1):
    if n % i == 0:
      contador += 1
      print(i, end=' ')

  print()
  print(f'Total: {contador} divisores')

main()