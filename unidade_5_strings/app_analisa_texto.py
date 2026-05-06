def main():
  texto = input('Texto: ')

  qtd_maiusculas = contar_maiusculas(texto)
  qtd_minusculas = contar_minusculas(texto)

  resultado = f'''
  >>> Resultado <<<
  Tamanho: {len(texto)} caracteres
  Letras Maiúsculas: {qtd_maiusculas}
  Letras Minúsculas: {qtd_minusculas}
  '''

  print(resultado)


def contar_maiusculas(texto):
  contador = 0

  for caractere in texto:
    if ord(caractere) >= 65 and ord(caractere) <= 90:
      contador += 1
  
  return contador


def contar_minusculas(texto):
  contador = 0

  for caractere in texto:
    if ord(caractere) >= 97 and ord(caractere) <= 122:
      contador += 1
  
  return contador


main()