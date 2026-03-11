def main():
  objetivo = float(input('Objetivo R$: '))

  contador_meses = 0
  poupanca = 0

  while poupanca < objetivo:
    valor = float(input('Valor poupado no mês (R$): '))
    poupanca = poupanca + valor
    print(f'Valor poupado ({poupanca/objetivo*100:.0f}%)')
    contador_meses = contador_meses + 1
  

  # Resultado
  print('Parabéns!! Você alcançou seu objetivo.')
  print(f'Objetivo R$: {objetivo:.1f}')
  print(f'Alcançado R$: {poupanca:.1f}')
  print(f'Quantidade meses: {contador_meses}')


main()