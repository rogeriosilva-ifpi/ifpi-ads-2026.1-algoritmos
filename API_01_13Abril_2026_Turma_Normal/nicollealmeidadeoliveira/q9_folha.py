from utils import obter_int_positivo, obter_texto


def main():
    n = obter_int_positivo('Quantos empregados? ')
     




def calcular(n):
    inss = 0
    desconto_vale = 0
    desconto_inss = 0

    for i in range(1, n + 1):
        nome = obter_texto('Nome: ')
        salario_bruto = float(input('Salário bruto: '))
        qtd_horas_extras = obter_int_positivo('Quantidade de horas extras: ')

        
        desconto_inss = (salario_bruto * 0.11)
        inss = salario_bruto - desconto_inss
        valor_horas_extras = qtd_horas_extras * (salario_bruto / 220)
        if salario_bruto > 2000:
            desconto_vale = salario_bruto - 150
            salario_liquido = (salario_bruto - inss - desconto_vale) + valor_horas_extras
            print(f'''----- Extrato {nome} -----
Salário_bruto ----- {salario_bruto}
Horas Extras ----- {qtd_horas_extras}
INSS ----- {inss}
''')
        else:
            salario_liquido

    
