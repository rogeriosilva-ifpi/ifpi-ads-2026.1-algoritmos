from utils_io import limpar_tela

def main():
    limpar_tela()

    distancia=float(input('Distância total(km): '))
    percent_estrada=int(input('Percentual da viagem em estrada(%): '))
    preco_combustivel=float(input('Preço do combústivel: '))

    trecho_estrada=(percent_estrada*distancia)/100
    trecho_cidade=distancia-trecho_estrada
    combustivel_estrada=trecho_estrada/12
    combustivel_cidade=trecho_cidade/8
    combustivel_total=combustivel_estrada+combustivel_cidade
    preco_total=combustivel_total*preco_combustivel

    print(f'Consumo em cidade: {combustivel_cidade:.2f}L')
    print(f'Consumo em estrada: {combustivel_estrada:.2f}L')
    print(f'Combustível total necessário para a viagem: {combustivel_total:.2f}L')
    print(f'Custo total: R${preco_total:.2f}')

main()