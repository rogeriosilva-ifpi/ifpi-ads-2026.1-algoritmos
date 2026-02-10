#Entrada

valor_mercadoria = float(input("Digite o valor da mercadoria: "))

#Processamento
parcela = valor_mercadoria // 3
entrada = parcela + (valor_mercadoria % 3)

#saída
print(f"O valor da entrada é {entrada} e o valor das parcelas é {parcela} ")