def main():

    aprovados = 0

    reprovados = 0

    recuperacao = 0

    soma = 0


    


    for n in range(1, 10 + 1):

        nota = float(input(f'Digite a nota do aluno n° {n}'))
        print()

        soma += nota

        if nota >= 7:

            aprovados += 1

            print(f'Aluno n° {n}>> aprovado')

        
        
        elif nota >= 5 and nota < 7:

            recuperacao += 1

            print(f'Aluno n ° {n}>>> recuperação')


        
        
        elif nota < 5:

            reprovados += 1

            print(f'Aluno n ° {n}>>> reprovado')



    media = soma / 10

    print()
    print(f'Média geral: {media}')
    print(f'Aprovados: {aprovados}')
    print(f'Reprovados: {reprovados}')
    print(f'Recuperação: {recuperacao}')




            



main()