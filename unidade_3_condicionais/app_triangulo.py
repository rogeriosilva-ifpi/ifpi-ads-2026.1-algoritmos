from utils_geometria_plana import eh_triangulo, obter_tipo_triangulo
from utils_io import escrever, obter_inteiro


def main():
  escrever('>>> App Triângulo <<<')

  lado_1 = obter_inteiro('Lado 1: ')
  lado_2 = obter_inteiro('Lado 2: ')
  lado_3 = obter_inteiro('Lado 3: ')

  # eh_triangulo = verificar_se_triangulo(lado_1, lado_2, lado_3)

  if eh_triangulo(lado_1, lado_2, lado_3):
    escrever('SIM. Os lados formam um triângulo.')
    tipo = obter_tipo_triangulo(lado_1, lado_2, lado_3)
    escrever(f'> E o tipo do triângulo é {tipo}.')
  else:
    escrever('NÃO. Os lados não formam um triângulo.')


# Executar o programa
main()