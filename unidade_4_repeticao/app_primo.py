def main():
  numero = int(input('Digite um número: '))

  while not eh_primo(numero):
    qtd_divisores = contar_divisores(numero)
    print(f'O número {numero} tem {qtd_divisores} divisores.')

    print('>>>')
    numero = int(input('Digite outro número: '))
  

  print('FIM. Você digitou um PRIMO.')


def eh_primo(numero):
  for candidato in range(2, numero//2 + 1):
    if numero % candidato == 0:
      return False
  
  return True
    

def contar_divisores(numero):
  contador = 0

  for i in range(1, numero + 1):
    if numero % i == 0: #eh_divisor?
      contador = contador + 1
  
  return contador


main()