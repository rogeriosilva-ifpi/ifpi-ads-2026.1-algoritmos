def main():
  n = int(input('N: '))

  soma = 0
  for i in range(1, n+1):
    soma = soma + 1/i

  print(f'S = {soma:.4f}') # f-string


main()