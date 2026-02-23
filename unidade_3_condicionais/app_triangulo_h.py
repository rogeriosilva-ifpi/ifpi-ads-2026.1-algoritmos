from utils_geometria_plana import eh_triangulo, obter_area_triangulo_by_heron
from utils_io import escrever, obter_inteiro


def main():
  escrever("*** App de Heron ***")

  r = obter_inteiro('Lado 1: ')
  s = obter_inteiro('Lado 2: ')
  t = obter_inteiro('Lado 3: ')

  if eh_triangulo(r, s, t):
    area = obter_area_triangulo_by_heron(r, s, t)
    resposta = f'É um triângulo de área igual a {area:.2f}'
    escrever(resposta)
  else:
    escrever('Não formam um triângulo!')



main()