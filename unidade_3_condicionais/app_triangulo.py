
def main():
  escrever('>>> App Triângulo <<<')

  lado_1 = obter_inteiro('Lado 1: ')
  lado_2 = obter_inteiro('Lado 2: ')
  lado_3 = obter_inteiro('Lado 3: ')

  eh_triangulo = verificar_se_triangulo(lado_1, lado_2, lado_3)

  if eh_triangulo == True:
    escrever('SIM. Os lados formam um triângulo.')
    tipo = verificar_tipo_triangulo(lado_1, lado_2, lado_3)
    escrever(f'\t > E o tipo do triângulo é {tipo}.')
  else:
    escrever('NÃO. Os lados não formam um triângulo.')


def escrever(conteudo):
  print(conteudo)


def obter_inteiro(instrucoes):
  numero = int(input(instrucoes))
  return numero


def verificar_se_triangulo(a, b, c):
  if c <= (a + b) and a <= (b + c) and b <= (a + c):
    return True
  else:
    return False
  

def verificar_tipo_triangulo(a, b, c):
  if a == b and a == c and b == c:
    return 'Equilátero'
  elif a != b and b != c and a != c:
    return 'Escaleno'
  else:
    return 'Isósceles'


# Executar o programa
main()