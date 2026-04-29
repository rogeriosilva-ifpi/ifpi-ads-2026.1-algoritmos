def main():
  n = int(input('N: '))
  m = int(input('M: '))
  soma = 0

  print('Números', end=' ')
  for i in range(n, m+1):
    if i % 2 != 0 and i % 3 == 0:
      soma += i
      print(i, end=' ')

  print()
  print(f'Soma: {soma}')

main()