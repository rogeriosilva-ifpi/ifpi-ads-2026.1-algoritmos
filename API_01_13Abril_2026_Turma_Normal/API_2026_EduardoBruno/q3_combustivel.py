def main():
    distancia_total = float(input('Distancia total: '))
    percentual_estrada = float(input('Percentual em estrada: '))
    preco_gaso = float(input('Preço do combustivel(R$): '))
    try:
        if distancia_total < 0 or percentual_estrada < 0 or preco_gaso < 0:
            print('Valor inválido!')
        else:
            estrada_km = (percentual_estrada * distancia_total / 100)
            cidade_km = distancia_total - estrada_km
            gaso_litros = (estrada_km / 12) + (cidade_km / 8)
            gasto_total = preco_gaso * gaso_litros
            print(f'Cidade: {cidade_km / 8:.1f} L')
            print(f'Estrada: {estrada_km / 8:.1f} L')
            print(f'Total de ltros: {gaso_litros:.1f} L')
            print(f'Custo total: R$ {gasto_total:.2f}')

    except ValueError:
        print('Digite um valor válido')
        



main()