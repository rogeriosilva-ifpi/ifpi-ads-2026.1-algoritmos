from utils import *

def main():
    total_km = obter_inteiro("Total(km): ")
    percentual_estrada = obter_real_intervalo('Percentual: ', 0, 100)
    preco_litro = obter_real("Preço(R$): ")
    
    percentual_cidade = 100 - percentual_estrada
    consumo_cidade = (total_km * percentual_cidade / 100) / 8
    consumo_estrada = (total_km * percentual_estrada / 100) / 12
    
    print(f'Consumo na estrada: {consumo_estrada:.1f}L')
    print(f'Consumo na cidade:  {consumo_cidade:.1f}L')
    print(f'Total de litros:    {consumo_estrada + consumo_cidade:.1f}L')
    print(f'Custo da viagem:    {(consumo_estrada + consumo_cidade) * preco_litro:.2f}R$') 
    

main()
    