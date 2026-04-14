def obter_inteiro():
    try:
        n = int(input())
    except:
        print("Insira um número inteiro: ", end='')
        n = int(input())
    return n


def obter_float():
    try:
        n = float(input())
    except:
        print("Insira um número float: ", end='')
        n = float(input())
    return n


def adicionar(n, m):
    soma = n + m
    return soma


def subtrair(n, m):
    subtracao = n - m
    return subtracao


def multiplicar(n, m):
    multiplicacao = n * m
    return multiplicacao


def dividir(n, m):
    divisao = n / m
    return divisao