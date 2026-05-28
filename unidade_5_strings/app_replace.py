def main():
    texto = input('Texto: ')
    substituido = input("Substituido: ")
    substituto = input('Substituto: ')

    texto_alta = replace(texto, substituido, substituto)

    print(texto_alta)


def replace(texto, substituido, substituto):
    novo_texto = ""
    for caracter in texto:
        if caracter == substituido:
            novo_texto = novo_texto + substituto
        else:
            novo_texto = novo_texto + caracter
    return novo_texto

main()