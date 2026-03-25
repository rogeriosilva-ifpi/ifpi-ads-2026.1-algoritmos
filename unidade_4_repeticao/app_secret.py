import random

def main():
  numero_sorteado = random.randint(1, 100)
  numero = int(input('Numero: '))
  pontuacao = 100
  contador = 1

  while numero != numero_sorteado and contador < 10:
    print('ERROU!!!')
    if numero_sorteado < numero:
      print('O número sorteado é MENOR que o número lido')
    else:
      print('O número sorteado é MAIOR que o número lido')

    numero = int(input('Novo número: '))
    contador = contador + 1
    pontuacao = pontuacao - 10

  if (contador < 10):
    print('ACERTOU!!')
  else:
    print('Você Perdeu!!') 

  print(f'> O número sorteado é {numero_sorteado}')
  print(f'> A pontuacao é {pontuacao}')

main()