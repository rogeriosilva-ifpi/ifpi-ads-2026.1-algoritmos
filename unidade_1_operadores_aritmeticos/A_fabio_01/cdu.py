# Entrada 
numero = int(input('Digite um número de 3 digitos: '))

# Processamento
centena = numero // 100
resto = numero % 100

dezena = resto // 10
unidade = resto % 10

somatorio = centena + dezena + unidade

# Saída
print(f'A soma dos dígitos do número {numero} é igual a {somatorio}')