def main():
  n = int(input('N: '))
  inferior = int(input('Inferior: '))
  superior = int(input('Superior: '))

  for valor in range(inferior, superior+1):
    if valor % n == 0:
      print(valor, end=' ')
    else:
      print('*', end=' ')


main()