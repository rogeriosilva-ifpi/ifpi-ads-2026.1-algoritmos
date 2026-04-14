def main(): 

    n_funcinario = int(input('Digite a quantidade de funcionários: '))
    print() 

    numero_funci = 0

    vale_refaicao = 0

    valor_total = 0





    while n_funcinario != 0:
        n_funcinario -= 1

        numero_funci += 1

        nome = input(f'Digite o nome do funcionário n° {numero_funci}')
        print()
        salario_bruto = float(input('Digite o salário bruto: '))

        valor_total += salario_bruto
        print()
        horas_extras = int(input('digite as hotras extras: '))
        print()

        if salario_bruto > 2000:
            vale_refaicao = 150


        elif salario_bruto < 2000: 
            vale_refaicao = 0





        valor_extra = salario_bruto / 220

        salario_extra = (valor_extra * (150/100)) * horas_extras


        inss = salario_bruto - (salario_bruto * 0.11)

        desconto = inss + vale_refaicao

        salario_liquido = salario_bruto - desconto



        print(f'---EXTRATO: {nome} ---- ')
        print(f'Salário Bruto: r$ {salario_bruto}')
        print(f'Horas extras: r$ {salario_extra}')
        print(f'INSS: {inss}')
        print(f'vale refaiçaõ: r$ {vale_refaicao}')
        print(f'Salário líquido: r$ {salario_liquido}')


    print(f'folha salarial')
    print(f'valor: {valor_total}')





















main()