# Entrada
cotacao = float(input('Cotação do Dólar: '))
total_dollar = float(input('Quantos dólares você tem? '))

# Processamento
total_reais = total_dollar * cotacao

# Saída
print(f'> US$ {total_dollar:.2f} equivalem a R$ {round(total_reais, 2)}. Pois a cotação está em US$/R$ {cotacao:.2f}')