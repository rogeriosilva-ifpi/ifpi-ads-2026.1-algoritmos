import os
from utils.os_utils import limpar_tela
from utils.number_utils import obter_inteiro


def obter_n_m():
    print("Insira um número inteiro N:", end=" ")
    n = obter_inteiro()
    print("Insira um número inteiro M maior que N:", end=" ")
    m = obter_inteiro()
    while m < n:
        print("M precisa ser maior que N.")
        print("Insira um número inteiro M maior que N:", end=" ")
        m = obter_inteiro()
    return n, m


def printar_impar_div_3(n, m):
    quant = 0
    for i in range(n, m):
        if i % 2 != 0:
            if i % 3 == 0:
                quant += 1
    if quant != 0:
        print("Números: ", end="")
        for i in range(n, m):
            if i % 2 != 0:
                if i % 3 == 0:
                    print(i, end=" ")
        print("")
    else:
        print("Nenhum número satisfaz a condição.")      
    

def printar_soma(n, m):
    soma = 0
    for i in range(n, m):
        if i % 2 != 0:
            if i % 3 == 0:
                soma += i
    if soma != 0:
        print("Soma: ", end="")
        print(soma)    


def main():
    limpar_tela()
    n, m = obter_n_m()
    printar_impar_div_3(n, m)
    printar_soma(n, m)


main()