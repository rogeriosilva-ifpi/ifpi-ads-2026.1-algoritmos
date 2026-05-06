def main():
  texto = input("Digite o texto: ")
  print(duplicar_tudo(texto))


def duplicar_tudo(texto):
  texto_duplicado = ""
  for i in texto:
    texto_duplicado += i + i
  return texto_duplicado


main()