def combusivel():

    distancia_total=float(input('Distancia Total: '))

    estrada=int(input('percentual do trecho em estrada: '))
    print(f'logo o percentual do trecho em cidade é {100-estrada}%')
    cidade_km=distancia_total-((estrada/100)*distancia_total)
    estrada_km=distancia_total-cidade_km
    valor_gasolina=float(input('valor do litrp do combustivel: '))
    gasolina_estrada=(estrada_km/12)*valor_gasolina
    gasolina_cidade=(cidade_km/8)*valor_gasolina
    total_litros=(estrada_km/12)+(cidade_km/8)
    custo=gasolina_estrada+gasolina_cidade

    print(f'o consumo do trecho de estrada foi de {gasolina_estrada}L')
    print(f'o consumo do trecho de cidade foi de {gasolina_cidade}L')
    print(f'o total de Litro necessáriosm para essa viagem é de {total_litros}L')
    print(f' o custo total da viagem foi de {custo}R$')



combusivel()