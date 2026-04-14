def main():
    distancia = float(input("Coloque a distância total em Km: "))
    percentual_BR = float(input("Coloque o percentual em estrada (0-100%): ")) / 100
    preco_litro = float(input("Coloque o preço do litro do combustível: "))
    
    percentual_rua = 1 - percentual_BR
    
    custo(distancia, percentual_BR, percentual_rua, preco_litro)

def custo(distancia, percentual_BR, percentual_rua, preco_litro):
    distancia_BR = distancia * percentual_BR
    distancia_rua = distancia * percentual_rua
    
    consumo_BR = 15  # km/l em BR
    consumo_rua = 20  # km/l em rua
    
    litros_BR = distancia_BR / consumo_BR
    litros_rua = distancia_rua / consumo_rua
    
    custo_BR = litros_BR * preco_litro
    custo_rua = litros_rua * preco_litro
    
    print(f"Estrada (BR): {distancia_BR:.2f} km, {litros_BR:.2f} l, R$ {custo_BR:.2f}")
    print(f"Rua: {distancia_rua:.2f} km, {litros_rua:.2f} l, R$ {custo_rua:.2f}")
    print(f"Total: {litros_BR + litros_rua:.2f} l, R$ {custo_BR + custo_rua:.2f}")

main()