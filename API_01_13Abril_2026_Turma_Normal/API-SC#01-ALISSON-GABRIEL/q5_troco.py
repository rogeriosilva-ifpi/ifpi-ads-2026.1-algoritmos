def main():
    qtd_produtos = int(input('Informe a quantia de produtos: '))

    total = 0
    troco = 0
    for i in range(0, qtd_produtos):
        preco = float(input('Preço produto: '))
        total += preco
    print(f'Valor total: R${total:.2f}')
    
    valor_pago = float(input('Informe o valor pago: R$'))

    if valor_pago >= total:
        troco = valor_pago - total

        troco_100 = troco // 100
        troco_50 = troco % 100 // 50
        troco_20 = troco % 50 // 20
        troco_10 = troco % 20 // 10
        troco_5 = troco % 10 // 5 
        troco_2 = troco % 5 // 2
        troco_1 = troco % 5 // 1
        troco_050 = troco % 1 // 0.5
        troco_025 = troco % 0.5 // 0.25
        troco_010 = troco % 0.25 // 0.10
        troco_005 = troco % 0.10 // 0.05
        troco_001 = troco % 0.05 // 0.01
        
        resultado = f'''
Seu troco é de: R${troco:.2f}
Será: {troco_100} notas de R$100, {troco_50} notas de 50, {troco_20} notas de 20, {troco_10} notas de 10, {troco_5} notas de 5, {troco_2} notas de 2 e {troco_1} notas de 1, {troco_050} de 0.50 centavos, {troco_025} de 0.25 centavos, {troco_010} de 0.10 centavos, {troco_005} de 0.05 centavos e {troco_001} de 0.01 centavos'''
        print(resultado)
    else: 
        print('Valor pago é insuficiente')

    



main()