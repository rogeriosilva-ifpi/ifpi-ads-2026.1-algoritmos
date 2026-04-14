import os
from utils.number_utils import obter_inteiro
from utils.os_utils import limpar_tela


def printar_divisores(n):
    print("Divisores: ", end="")
    for i in range(1, n + 1):
        if n % i == 0:
            if i != n:
                print(i, end=" ")
            elif i == n:
                print(i)


def printar_total(n):
    total_divisores = 0
    print("Total: ", end="")
    for i in range(1, n + 1):
        if n % i == 0:
            total_divisores += 1
    print(f"{total_divisores} divisores.")


def main():
    limpar_tela()
    print("Insira um número inteiro: ", end="")
    n = obter_inteiro()
    printar_divisores(n)
    printar_total(n)


main()