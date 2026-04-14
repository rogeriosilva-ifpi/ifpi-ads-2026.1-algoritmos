def main():
    total_km = float(input('Distância total em km: '))
    percentual = float(input('Percentual em estrada: '))
    percentual /= 100
    preco = float(input('Preço do litro de combustível em R$: '))

    km_estrada = total_km * percentual
    km_cidade = total_km - km_estrada

    estrada_rs = calcular_consumo(km_estrada, preco)
    cidade_rs = calcular_consumo(km_cidade, preco)
    total = estrada_rs + cidade_rs

    print(f'Consumo estrada: {estrada_rs:.2f}R$\nConsumo cidade: {cidade_rs:.2f}R$\nConsumo total: {total:.2f}R$.')

def calcular_consumo(km, rs):
    return km * rs

main()