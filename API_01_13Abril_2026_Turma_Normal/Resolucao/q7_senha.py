from utils import obter_inteiro_faixa


def main():
  senha = ''
  digito_anterior = None
  senha_valida = True
  motivo = ''
  soma_digitos = 0

  for i in range(6):
    digito_atual = obter_inteiro_faixa(f'Dígito {i+1}: ', 0, 9)
    soma_digitos += digito_atual

    if i >= 1:
      if digito_atual == digito_anterior:
        motivo += '> Dígito repetido\n'
        senha_valida = False
    
    if i == 0 and digito_atual == 0:
      motivo += '> Primeiro dígito é zero \n'
      senha_valida = False

    senha += str(digito_atual)
    digito_anterior = digito_atual

  # Valida soma
  if soma_digitos <= 20:
    motivo += '> Soma dos dígitos igual ou menor à 20'
    senha_valida = False
  
  print(f'Senha digitada: {senha}')
  print(f'Senha válida? ', senha_valida)
  
  if not senha_valida:
    print(motivo)


main()