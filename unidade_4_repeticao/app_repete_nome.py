def main():
  nome = input('Qual seu nome? ')
  quantidade = int(input('Quantas vezes? '))

  # FOR e WHILE
  for i in range(quantidade):
    if i % 2 == 0:
      print(i, nome)
    else:
      print(nome)
  

main()