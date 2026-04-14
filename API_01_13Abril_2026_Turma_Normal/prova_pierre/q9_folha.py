def main():
    n = int(input('N de funcionários: '))
    menor_s = None
    maior_s = 0
    contador = 0
    nome = ''
    s_bruto = 0
    h_extras = 0
    while contador < n:
        try:
            nome = input('Nome: ')
            s_bruto = float(input('Salario bruto: '))
            h_extras = float(input('Horas extras:'))

            if menor_s == None:
                menor_s = s_bruto
            if s_bruto < menor_s:
                menor_s = s_bruto
            if s_bruto > maior_s:
                maior_s = s_bruto
            print(extrato(s_bruto, h_extras, nome))
            contador += 1
        except:
            print('Incorreto, digite novamente: ')

    print(f'Menor salário bruto: {menor_s:.2f}')
    print(f'Maior salário bruto: {maior_s:.2f}')



def extrato(s, v, n):
    horas = (s / 220) * 1.5
    inss = s * 0.11
    if s > 2000:
        vr = 150
    else:
        vr = 0
    sl = s + horas - inss - vr
    return f'''
--Extrarto: {n}----
Salario Bruto: R$ {s:.2f}
Horas extras: R$ {horas:.2f} ({v:.0f}h)
INSS: R${inss:.2f}
Vale Refeição: R${vr:.2f}
Salário Líquido: R${sl:.2f}'''


main()