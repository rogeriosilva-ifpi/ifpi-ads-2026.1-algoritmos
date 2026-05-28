def main():
    texto = input('Texto: ')

    texto_alta = upper(texto)

    print(texto_alta)


def upper(texto):
    novo_texto = ''
    for caracter in texto:
        codigo = ord(caracter)
        if codigo >= 97 and codigo <= 122: # é letra minúscula
            novo_codigo = codigo - 32
            novo_caracter = chr(novo_codigo)
            novo_texto = novo_texto + novo_caracter
        else:
            novo_texto = novo_texto + caracter
    
    return novo_texto


main()