from utils import obter_inteiro_faixa, obter_real_positivo, obter_real_minimo
import os


def main():
  menu = '''
  >>> Kasse <<<
  1 - Incluir Produto
  2 - Ver Conta
  3 - Pagar
  ----
  0 - Sair > '''
  conta = 0.0

  opcao = obter_inteiro_faixa(menu, 0, 3)

  while opcao != 0:

    if opcao == 1:
      valor_produto = obter_real_positivo('Valor do Produto: ')
      conta += valor_produto
    elif opcao == 2:
      print(f'Valor da conta: {conta:.2f}')
    elif opcao == 3:
      print(f'Valor da conta: {conta:.2f}')
      valor_recebido = obter_real_minimo('Valor (R$): ', conta)
      mostrar_troco(conta, valor_recebido)
      conta = 0
    
    input('Enter...')
    os.system('clear')
    opcao = obter_inteiro_faixa(menu, 0, 3)


def mostrar_troco(conta, valor_recebido):

  troco = valor_recebido - conta

  ced_100 = troco // 100
  saldo = troco % 100
  
  ced_50 = saldo // 50
  saldo = saldo % 50
  
  ced_20 = saldo // 20
  saldo = saldo % 20

  ced_10 = saldo // 10
  saldo = saldo % 10

  ced_5 = saldo // 5
  saldo = saldo % 5

  ced_2 = saldo // 2
  saldo = saldo % 2

  #  Moedas
  saldo = saldo * 100
  moeda_50 = saldo // 50
  saldo = saldo % 50

  moeda_25 = saldo // 25
  saldo = saldo % 25

  moeda_10 = saldo // 10
  saldo = saldo % 10

  moeda_5 = saldo // 5
  moeda_1 = saldo % 5

  resultado_troco = f'''
  Troco: R$ {troco:.2f}
  Cédula de R$ 100 = {ced_100:.1f}
  Cédula de R$ 50 = {ced_50:.1f}
  Cédula de R$ 20 = {ced_20:.1f}
  Cédula de R$ 10 = {ced_10:.1f}
  Cédula de R$ 5 = {ced_5:.1f}
  Cédula de R$ 2 = {ced_2:.1f}
  Moedas de R$ 0,50 = {moeda_50:.1f}
  Moedas de R$ 0,25 = {moeda_25:.1f}
  Moedas de R$ 0,10 = {moeda_10:.1f}
  Moedas de R$ 0,05 = {moeda_5:.1f}
  Moedas de R$ 0,01 = {moeda_1:.1f}
  '''

  print(resultado_troco)


main()