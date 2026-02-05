# Entrada
# real float(), int(), str()
limite_inferior = int(input('Digite o limite inferior(M): '))
limite_superior = int(input('Digite o limite superior(N): '))


# Processamento
soma_dos_pares = limite_inferior + limite_superior
quantidade_de_pares = (limite_superior - limite_inferior + 1) / 2

somatorio = soma_dos_pares * quantidade_de_pares

# Saída (f-string)
print(f'O somatório de {limite_inferior} até {limite_superior} é {somatorio}')
