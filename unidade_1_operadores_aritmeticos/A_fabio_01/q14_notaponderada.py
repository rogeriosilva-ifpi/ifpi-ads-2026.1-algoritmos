#entrada
nota_1 = float(input("Insira a primeira nota: "))
peso_1 = float(input("Insira o peso da primeira nota: "))
nota_2 = float(input("Insira a segunda nota: "))
peso_2 = float(input("Insir o peso da segunda nota: "))
nota_3 = float(input("Insira a terceira nota: "))
peso_3 = float(input("Insira o peso da terceira nota: "))

#processamento
media = (nota_1 * peso_1) + (nota_2 * peso_2) + (nota_3 * peso_3)
media_ponderada = media / (peso_1 + peso_2 + peso_3)

#saída
print(f"> A média ponderada é {media_ponderada}.")