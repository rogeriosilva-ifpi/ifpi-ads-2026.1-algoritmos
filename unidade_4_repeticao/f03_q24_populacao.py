def main():
  n = int(input('Quantos entrevistados? '))

  soma_salarios = 0
  soma_filhos = 0
  contar_salarios_ate1000 = 0

  for i in range(n):
    # Entrevista i
    salario = float(input(f'{i} > Salario: '))
    filhos = int(input(f'{i} > Filhos: '))

    if salario <= 1000:
      contar_salarios_ate1000 = contar_salarios_ate1000 + 1

    soma_salarios = soma_salarios + salario
    soma_filhos = soma_filhos + filhos

  # Computações
  media_salarial = soma_salarios / n
  media_filhos = soma_filhos / n
  percentual_ate1000 = (contar_salarios_ate1000 / n) * 100

  print('Resultado')
  print(f'> Média de salário da população = R$ {media_salarial:.2f}')
  print(f'> Média de número de filhos = {media_filhos:.1f}')

  # '> Pessoas que ganham até R$ 1000: 7 (42.0%)'
  print(f'> Pessoas que ganham até R$ 1000: {contar_salarios_ate1000} ({percentual_ate1000:.1f} %)')
  


main()