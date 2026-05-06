def main():
  texto = input('Texto: ')

  for i in range(len(texto)):
    print(i, texto[i], ord(texto[i]))

  print(f'O texto digitado tem {len(texto)} caracteres')


main()