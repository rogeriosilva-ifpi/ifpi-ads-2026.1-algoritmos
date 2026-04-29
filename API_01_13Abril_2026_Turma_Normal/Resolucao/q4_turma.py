
def main():
  n = int(input('Quantos alunos? '))
  maior_nota = 0
  menor_nota = 10
  somatorio = 0
  contador_ap = 0
  contador_rp = 0
  contador_rc = 0

  for i in range(n):
    nota = float(input(f'Nota (Aluno: {i+1}): '))
    somatorio += nota
    if nota > maior_nota:
      maior_nota = nota
    
    if nota < menor_nota:
      menor_nota = nota

    situacao = computador_situacao(nota)
    print(f'Situação: {situacao}')

    if situacao == 'Aprovado':
      contador_ap += 1
    elif situacao == 'Em recuperação':
      contador_rc += 1
    else:
      contador_rp += 1

  media = somatorio / n  
  resultado = f'''
  >> Resultado Turma <<
  Maior Nota: {maior_nota}
  Menor Nota: {menor_nota}
  Nota Média: {media:.1f}
  Resumo:
  Aprovados: {contador_ap}
  Em recuperação: {contador_rc}
  Reprovados: {contador_rp}
  '''

  print(resultado)


def computador_situacao(nota):
  if nota >= 7:
    return 'Aprovado'
  elif nota >= 5:
    return 'Em recuperação'
  else:
    return 'Reprovado'

main()