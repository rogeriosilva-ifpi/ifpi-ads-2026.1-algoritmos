from utilitaros import inteiro, positivo

def main():
    quant_prod = inteiro('quantos produtos? ')
    valor_total = 0
    for i in range(1,quant_prod+1):
        preco = positivo(f'preco do produto {i}: ')
        valor_total += preco

    print(f'valor total: R${valor_total}')

    valor_pago = positivo('qual o valor do pagamento? ')

    while valor_pago < valor_total:
        print('o valor é insuficiente...')
        valor_pago = positivo('qual o valor do pagamento? ')


    if valor_pago > valor_total:
        resto = valor_pago - valor_total
        print(f'pagamento efetuado: {valor_pago}\nVocê tem R${resto} de troco.')




main()