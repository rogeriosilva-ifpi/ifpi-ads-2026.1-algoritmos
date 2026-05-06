def main():
  inicio = int(input('Início: '))
  fim = int(input('Fim: '))

  escrever_ascii(inicio, fim)
  


def escrever_ascii(inicio, fim):
  print('>>> ASCII Table <<<<')

  for i in range(inicio, fim+1):
    print(i, chr(i))


main()