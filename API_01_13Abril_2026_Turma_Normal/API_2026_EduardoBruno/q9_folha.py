def main():
    quant_funcionarios = int(input('Quantidade: '))
    try:
        for i in range(1,quant_funcionarios+1):
            nome = input('Nome: ').upper().strip()
            salario_bruto = float(input('Salario bruto: '))
            horas_extra = int(input('Horas extras: '))
            uma_hora_extra = ((salario_bruto / 220)* 2.5)
            inss = 0.11 * salario_bruto
            print(f'--- EXTRATO: {nome} ---')
            print(f'Salário Bruto: R$ {salario_bruto:.2f}')
            print(f'Horas Extras: R$ {uma_hora_extra * horas_extra:.2f}')
            print(f'INSS: R$ {inss:.2f}')
            if salario_bruto > 2000:
                vale = 150
                print(f'Vale Refeição: R$ {vale:.2f}')
            else:
                vale = 0
            salario_liquido = (salario_bruto + horas_extra - inss - vale)
            print(f'Salário Líquido: R$ {salario_liquido:.2f}')
    except ValueError:
        print('Digite corretamente!')



main()