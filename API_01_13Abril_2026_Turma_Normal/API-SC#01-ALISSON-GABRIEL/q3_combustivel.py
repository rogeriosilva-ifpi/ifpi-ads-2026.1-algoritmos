def main():
    km = int(input('Informe a distância em km: '))
    percentual_estrada = int(input('Informe o percentual em estrada:% '))
    valor_litro = float(input('Informe o valor do litro do combustível:R$ '))

    consumo_estrada = km * percentual_estrada / 100
    consumo_cidade = km - consumo_estrada

    litros_estrada = consumo_estrada / 12
    litros_cidade = consumo_cidade / 8
    total_litros = litros_cidade + litros_estrada

    custo_total = (litros_cidade * valor_litro) + (litros_estrada * valor_litro)

    contrato = f'''
Contrato Translado:
Consumo na estrada: {litros_estrada:.2f}l
Consumo na cidade: {litros_cidade:.2f}l
Litros de combustível necessário: {total_litros:.2f}
Custo total: R${custo_total:.2f}'''
    print(contrato)



main()