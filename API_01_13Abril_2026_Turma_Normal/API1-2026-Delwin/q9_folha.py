from utils import obterInteiro, obterFloat

def Main():
    #Chamando obter inteiro para pedir número 
    n = obterInteiro('Digite o número de funcionários: ')
    
    for i in range(n):
        nome = input('Digite o nome do funcionário: ')
        salario_bruto = obterFloat('Digite o salário: ')
        hora_extra = obterInteiro('Digite a quantidade de horas extras: ')

        valor_hora_extra = salario_bruto / 220 * 1.5
        inss = salario_bruto * 0.11
        vr = 0
        if salario_bruto > 2000:
            vr = 150
        
        print(f'--- EXTRATO: {nome} ---')
        print(f'Salário bruto: R${salario_bruto}')
        print(f'Horas extras: R${valor_hora_extra}')
        print(f'INSS: R${inss}')
        print(f'Salário líquido: R${salario_bruto - inss - vr + valor_hora_extra}')
        print('---')



Main()