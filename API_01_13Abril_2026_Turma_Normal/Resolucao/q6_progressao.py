from utils import obter_inteiro_minimo, obter_inteiro_positivo


def main():
  pa()
  continuar = input('Mais uma PA? S-SIM ou N-NÃO: \n> ').upper()

  while continuar == 'S':
    pa()
    continuar = input('Mais uma PA? S-SIM ou N-NÃO')
  

  print("Chiao!")


def pa():
  primeiro_termo = obter_inteiro_positivo('Primeiro Termo: ')
  razao = obter_inteiro_positivo('Razao: ')
  quantidade = obter_inteiro_minimo('Quantidade de Termos: ', 2)

  termo_atual = primeiro_termo
  somatorio = 0
  for i in range(quantidade):
    somatorio += termo_atual
    print(termo_atual, end=' ')
    termo_atual += razao

  print('Fim')
  media = somatorio / quantidade
  print(f'Soma dos Termos: {somatorio}')
  print(f'Média: {media:.1f}')


main()