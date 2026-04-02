from io_utils import obter_inteiro
import os


def main():
  limpar_tela()
  numero = 10
  opcao = obter_inteiro(menu(numero))

  while opcao != 0:
    if opcao == 1:
      numero = obter_inteiro('Novo Número: ')
    elif opcao == 2:
      binario = converter_dec_bin(numero)
      print(f'O número {numero} em binário é "{binario}"')
    else:
      ...

    enter_to_continue()
    limpar_tela()

    opcao = obter_inteiro(menu(numero))


def menu(n: int):
  return f'''
  **** Conveter Sistemas Numéricos ****
  1 - Alterar Número (atual: {n})
  2 - Exibir em Binário
  3 - Exibir em Octal
  4 - Exibir em Hexadecimal
  -------------------------------------
  0 - Sair > '''

def limpar_tela():
  os.system('clear')


def enter_to_continue():
  input('<Enter> to continue...')


def converter_dec_bin(valor):
  resultado = ''
  resto = valor % 2
  quociente = valor // 2

  resultado = str(resto) + resultado

  while quociente > 0:
    resto = quociente % 2
    quociente = quociente // 2

    resultado = str(resto) + resultado

  return resultado

main()