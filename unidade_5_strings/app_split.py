def Main():
    texto = input('Digite o texto: ')
    separador = input('Digite o separador: ')

    pedacos = split(texto, separador)
    print(pedacos)

def split(texto, separador):
    pedacos = []
    texto_temporario = ''

    for i in texto:
        if i == separador:
            pedacos.append(texto_temporario)
            texto_temporario = ''
        else:
            texto_temporario += i

    pedacos.append(texto_temporario)

    return pedacos


Main()