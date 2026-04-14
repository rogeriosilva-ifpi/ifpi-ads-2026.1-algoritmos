def calcular_custo_viagem():
    distancia = float(input("Digite a distância total da viagem (km): "))
    percentual_estrada = float(input("Digite o percentual percorrido em estrada (0 a 100): "))
    preco_combustivel = float(input("Digite o preço do litro do combustível (R$): "))

    if percentual_estrada < 0 or percentual_estrada > 100:
        print("Erro: O percentual deve estar entre 0 e 100!")
    else:
        dist_estrada = distancia * (percentual_estrada / 100)
        dist_cidade = distancia - dist_estrada
        litros_estrada = dist_estrada / 12
        litros_cidade = dist_cidade / 8
        total_litros = litros_estrada + litros_cidade
        custo_total = total_litros * preco_combustivel
        
        print("\n--- RESUMO DO CUSTO ---")
        print("Distância na estrada:", dist_estrada, "km")
        print("Distância na cidade:", dist_cidade, "km")
        print(f"Litros na estrada: {litros_estrada:.2f} L")
        print(f"Litros na cidade: {litros_cidade:.2f} L")
        print(f"Total de litros necessários: {total_litros:.2f} L")
        print(f"Custo total da viagem: R$ {custo_total:.2f}")

calcular_custo_viagem()