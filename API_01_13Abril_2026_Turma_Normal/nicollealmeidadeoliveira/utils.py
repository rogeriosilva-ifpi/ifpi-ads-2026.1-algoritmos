def obter_inteiro(instrucoes='Digite um número inteiro: '):
    while True:
        try:
            n = int(input(instrucoes))
            return n
        except ValueError:
            continue


def obter_int_positivo(instrucoes='Digite um número inteiro positivo: '):
    while True:
        n = obter_inteiro(instrucoes)
        if n < 0:
            continue
        return n
    
def obter_texto(instrucoes='Digite um texto: '):
    texto = input(instrucoes)
    return texto


def main():
    n = obter_int_positivo('Digite um número: ')
    print(n)

if __name__ == "__main__":
    main()