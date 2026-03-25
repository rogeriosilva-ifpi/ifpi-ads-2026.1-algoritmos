# 10. Leia LimiteSuperior e LimiteInferior e 
# escreva todos os números ímpares entre os limites lidos.

from io_utils import *

def main():
  inferior = obter_inteiro_positivo('Inferior: ')
  superior = obter_inteiro_min('Superior: ', inferior + 1)

  for i in range(inferior, superior + 1):
    if i % 2 != 0:
      print(i, end=' ')
  
  print('Fim.')


main()