def main():
    distancia_total = validar_valor_positivo("\nDigite a distancia total da viagem, em km: ")
    percentual_estrada = validar_percentual("Digite, em porcentagem, o tamanho do trecho de estrada: ")
    preco_combustivel = validar_valor_positivo("Digite o valor do preço do combustível, em reais: ")
    
    distancia_estrada= distancia_total * percentual_estrada 
    distancia_cidade= distancia_total * (1 - percentual_estrada)
    consumo_estrada = consumo(distancia_estrada, 12)
    consumo_cidade = consumo(distancia_cidade, 8)
    consumo_total = consumo_estrada + consumo_cidade
    custo = (consumo_estrada + consumo_cidade) * preco_combustivel

    print(f"\nO consumo no trecho da estrada é {consumo_estrada:.2f} L e para o trecho da cidade é {consumo_cidade:.2f} L.")
    print(f"O total de litros de combustivel necessário é: {consumo_total:.2f} L")
    print(f"Por fim o custo da viagem ficou {custo:.2f} R$")


def consumo(distancia,consumo_kml):
    return distancia / consumo_kml


def validar_valor_positivo(instruções):
    valor = float(input(instruções))
    
    if valor < 0:
        while valor < 0:
            valor = float(input("Valor digitado não é valido. Digite um novo valor: "))
    else:
     return valor


def validar_percentual(instruções):
    valor = float(input(instruções))

    if valor < 0:
        while valor < 0:
            valor = float(input("Valor digitado não é valido. Digite um novo valor: "))
    else:
        if valor >100:
            while valor >100:
                valor = float(input("Valor digitado não é valido. Digite um novo valor: "))
        else:
            return valor / 100
        



main()