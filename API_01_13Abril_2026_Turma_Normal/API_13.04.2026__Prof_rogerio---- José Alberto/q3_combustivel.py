def main():

    print('***combutível***')

    print()

    km_distancia = float(input('Digite a ditância: '))
    print()
    litros_perco = float(input('Digite o preço do combutível em litros: '))
    print()
    porcen_cidade = float(input('Digite o percentuaal na cidade(%): '))
    print()
    porcen_estrada = float(input('Digite o percentual na estrada(%): '))

    print()

    pocetagem_cidade(km_distancia, porcen_cidade, litros_perco)
    print()
    porcentagem_estrada(km_distancia, porcen_estrada, litros_perco)















def pocetagem_cidade(distacia, pocentagem, preco_combu):

    porcetagem_valor = distacia * (pocentagem / 100)

    litros = porcetagem_valor  / 8

    combustivel_rs = litros * preco_combu

    

    print()
    print(f'ciade Valor R$: {combustivel_rs: .2f}')
    print()
    print(f'Litros: {litros: .2f}')
    print()




def porcentagem_estrada(distancia, porcentagem, preco_combus):

    porcentagem_valor = distancia * (porcentagem/ 100)

    litros = porcentagem_valor / 12

    combustivel_rs = litros * preco_combus

    

    
    print()
    print(f'estrada Valor R$: {combustivel_rs: .2f}')
    print(f'Litros: {litros: .2f}')
    print()







main()