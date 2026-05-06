def main():
  texto = input('Texto: ')

  sem_espacos = remover_espacos(texto)

  print(sem_espacos)


def remover_espacos(texto):
  novo_texto = ''

  for c in texto:
    if not c == ' ':
      novo_texto = novo_texto + c
  
  return novo_texto

main()