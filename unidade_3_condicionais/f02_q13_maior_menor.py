def main():
  num_1 = int(input('Número 1: '))
  num_2 = int(input('Número 2: '))
  num_3 = int(input('Número 3: '))
  num_4 = int(input('Número 4: '))
  num_5 = int(input('Número 5: '))

  maior = maximo(num_1, num_2, num_3, num_4, num_5)
  menor = minimo(num_1, num_2, num_3, num_4, num_5)
  
  print(f'O maior número é {maior}')
  print(f'O menor número é {menor}')


def maximo(num_1, num_2, num_3, num_4, num_5):
  if eh_maior_que_demais(num_1, num_2, num_3, num_4, num_5):
    return num_1
  elif eh_maior_que_demais(num_2, num_1, num_3, num_4, num_5):
    return num_2
  elif eh_maior_que_demais(num_3, num_2, num_1, num_4, num_5):
    return num_3
  elif eh_maior_que_demais(num_4, num_2, num_3, num_1, num_5):
    return num_4
  else:
    return  num_5
  

def minimo(num_1, num_2, num_3, num_4, num_5):
  if eh_menor_que_demais(num_1, num_2, num_3, num_4, num_5):
    return num_1
  elif eh_menor_que_demais(num_2, num_1, num_3, num_4, num_5):
    return num_2
  elif eh_menor_que_demais(num_3, num_2, num_1, num_4, num_5):
    return num_3
  elif eh_menor_que_demais(num_4, num_2, num_3, num_1, num_5):
    return num_4
  else:
    return  num_5


def eh_maior_que_demais(n1, n2, n3, n4, n5):
  return n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5
  

def eh_menor_que_demais(n1, n2, n3, n4, n5):
  return n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5
 

main()