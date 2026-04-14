def main():
    distancia_total = int(input("Digite a distânca total em Km: "))
    percentual = int(input("Digite o percentual desse percurso que é estrada (0 a 100): ")) / 100
    preco_litro = float(input("Digite o preço do litro combustível: "))
    estrada = distancia_total * percentual
    cidade = distancia_total - estrada
    percurso_estrada = calcular_consumo(estrada, 12)
    percurso_cidade = calcular_consumo(cidade, 8)
    litros = percurso_estrada + percurso_cidade
    custo_viagem = litros * preco_litro
    print(f"Consumo Cidade: {percurso_cidade:.2f}")
    print(f"Consumo Estrada: {percurso_estrada:.2f}")
    print(f"Litros de combustível necessários: {litros:.2f}")
    print(f"Custo viagem: R$ {custo_viagem:.2f}")



def calcular_consumo(percurso, consumo):
    litros = percurso / consumo
    return litros 





main()