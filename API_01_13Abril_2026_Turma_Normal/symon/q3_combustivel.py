def insformacao_viagem(km, per, preço_litro):

    km_estrada = per * 100 / km 
    km_cidade = km - km_estrada
    if km_cidade < 0:
        km_cidade *= -1

    consumo_estrada = km_estrada / 12
    consumo_cidade = km_cidade / 8

    total_litros = consumo_estrada + consumo_cidade

    custo = total_litros * preço_litro

    return f"Consumo de combustível na estrada: {consumo_estrada:.2f}L, Consumo de combustível na cidade: {consumo_cidade:.2f}L, Total de litros: {total_litros:.2f}L, Custo da viagem: {custo:.2f}R$"

# res = insformacao_viagem(100, 45, 5)
# print(res)

def main():
    try:
        distancia = float(input("Digite a distância total da viagem: "))
        percentual_estrada = float(input("Digite o tanto dela que será percorrida em 'estrada': "))
        preco_litro = float(input("Digite o valor do litro de combustível: "))
        res = insformacao_viagem(distancia, percentual_estrada, preco_litro)
        print(res)
    except:
        print("Digite valores válidos.")

if __name__ == "__main__":
    main()
    