def main():
  num_1 = int(input('Digite um número inteiro: '))
  num_2 = int(input('Digite um número inteiro: '))
  num_3 = int(input('Digite um número inteiro: '))
  num_4 = int(input('Digite um número inteiro: '))
  num_5 = int(input('Digite um número inteiro: '))
  
  maior = obter_maior_numero(num_1, num_2, num_3, num_4, num_5)
  menor = obter_menor_numero(num_1, num_2, num_3, num_4, num_5)
  
  print(f'O maior número = {maior}')
  print(f'O menor número = {menor}')


def obter_maior_numero(n1, n2, n3, n4, n5):
  maior = n1
  if n2 > maior:
    maior = n2
  
  if n3 > maior:
    maior = n3
  
  if n4 > maior:
    maior = n4
  
  if n5 > maior:
    maior = n5
  
  return maior


def obter_menor_numero(n1, n2, n3, n4, n5):
  menor = n1
  if n2 < menor:
    menor = n2
  
  if n3 < menor:
    menor = n3
  
  if n4 < menor:
    menor = n4
  
  if n5 < menor:
    menor = n5
  
  return menor


main()