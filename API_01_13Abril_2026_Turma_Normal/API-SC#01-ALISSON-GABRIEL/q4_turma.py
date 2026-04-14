def main():
    alunos = int(input('Informe a qunatia de alunos: '))
    
    media = 0
    qtd_reprovados = 0
    qtd_aprovados = 0
    qtd_recuperacao = 0
    contador = 0
    maior_nota = 0
    menor_nota = 0

    while contador < alunos:
        nota = float(input('Informe sua nota: '))
        media += nota / alunos
        contador += 1
        if nota > maior_nota:
            maior_nota = nota
        if nota < maior_nota:
            menor_nota = nota
        if nota >= 7:
            print('Aprovado')
            qtd_aprovados += 1
        elif nota >= 5:
            print('Recuperação')
            qtd_recuperacao += 1
        else:
            print('Reprovado')
            qtd_reprovados += 1
    resultado = f'''
A maior nota foi: {maior_nota}
A menor nota foi: {menor_nota}
A média da turma: {media:.2f}
Alunos aprovados: {qtd_aprovados}
Alunos de recuperação: {qtd_recuperacao}
Alunos reprovados: {qtd_reprovados}'''
    print(resultado)
    

main()