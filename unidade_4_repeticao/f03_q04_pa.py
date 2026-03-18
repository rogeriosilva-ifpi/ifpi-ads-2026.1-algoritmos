def main():
  inicial = int(input('Inicial: '))
  razao = int(input('Razão: '))
  limite = int(input('Limite: '))

  for numero in range(inicial, limite, razao):
    print(numero, end='-')
  
  print('Fim.')


main()