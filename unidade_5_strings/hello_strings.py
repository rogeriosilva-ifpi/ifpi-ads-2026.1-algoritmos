def main():
  nome = input('Nome: ')
  em_caixa_alta = upper(nome)
  qtd_digitos = contar_digitos(nome)
  print(em_caixa_alta)
  print(f'O nome digitado tem {qtd_digitos} dígitos(números)')


def upper(nome):
  novo_nome = ''
  for caractere in nome:
    novo_nome += upper_caractere(caractere)
  
  return novo_nome


def upper_caractere(caractere):
  if eh_letra_minuscula(caractere):
    novo_codigo = ord(caractere) - 32
    novo_caractere = chr(novo_codigo)
    return novo_caractere
  else:
    return caractere


def eh_letra_minuscula(caractere):
  return ord(caractere) >= 97 and ord(caractere) <= 122


def eh_vogal(caractere):
  vogais = 'aeiouAEIOU'
  for vogal in vogais:
    if caractere == vogal:
      return True
  
  return False



main()