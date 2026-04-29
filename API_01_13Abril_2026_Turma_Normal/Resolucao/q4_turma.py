from utils import obter_inteiro_positivo, obter_real_faixa

def main():
  n =  obter_inteiro_positivo('Quantos alunos? ')
  maior = -1
  menor = -1
  somatorio_geral = 0
  contador_ap = 0
  contador_rp = 0
  contador_rc = 0


  for i in range(n):
    nota = obter_real_faixa(f'Nota do aluno {i+1}: ', 0, 10)
    somatorio_geral += nota
    situacao = calcular_situacao(nota)
    if nota > maior:
      maior = nota
    
    if menor == -1 or nota < menor:
      menor = nota

    if situacao == 'AP':
      contador_ap += 1
    elif situacao == 'RP':
      contador_rp += 1
    else:
      contador_rc += 1
  
  media_turma = somatorio_geral / n

  resultado = f'''
  >>> RESULTADO <<<
  Maior nota: {maior}
  Menor nota: {menor}
  Média turma: {media_turma}
  ... Quant. por Situacao:
  Aprovados: {contador_ap}
  Em Recuperacão: {contador_rc}
  Reprovados: {contador_rp}
  '''

  print(resultado)


def calcular_situacao(nota):
  if nota < 5:
    return 'RP'
  elif nota < 7:
    return 'RC'
  else:
    return 'AP'


main()