from utils import *

def main():
    valor_total = 0
    
    while True:
        preco_produto = obter_real('Preço do produto(R$): ')
        
        if preco_produto == 0:
            break
        
        valor_total += preco_produto
    
    pagamento = obter_real_minimo('Pagamento(R$): ', valor_total)
    
    notas_100 = pagamento // 100
    resto_100 = pagamento % 100
    notas_50 = resto_100 // 50
    resto_50 = resto_100 % 50
    notas_20 = resto_50 // 20
    resto_20 = resto_50 % 20
    notas_10 = resto_20 // 10
    resto_10 = resto_20 % 10
    notas_5 = resto_10 // 5
    resto_5 = resto_10 % 5
    notas_2 = resto_5 // 2
    resto_2 = resto_5 % 2
    notas_1 = resto_2 // 1
    resto_1 = resto_2 % 1
    
    print('--- Troco detalhado ---')
    print(f'Notas 100: {notas_100}')
    print(f'Notas 50:  {notas_50}')
    print(f'Notas 20:  {notas_20}')
    print(f'Notas 10:  {notas_10}')
    print(f'Notas 5:   {notas_5}')
    print(f'Notas 2:   {notas_2}')
    print(f'Notas 1:   {notas_1}')
    print(f'Moedas:    {resto_1}')