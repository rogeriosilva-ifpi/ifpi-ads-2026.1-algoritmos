import os
from utils.os_utils import limpar_tela
from utils.number_utils import obter_inteiro


def obter_termos():
    print("Insira o primeiro termo (a): ", end="")
    a = obter_inteiro()
    print("Insira a razão (r): ", end="")
    r = obter_inteiro()
    print("Insira o número máximo de termos (n, mínimo de 2): ", end="")
    n = obter_inteiro()
    while n < 2:
        print("O número total de termos precisa ser igual ou maior que 2.")
        print("Insira o número máximo de termos (n, mínimo de 2): ", end="")
        n = obter_inteiro()
    return a, r, n


def exibir_progressao_arit(a, r, n):
    soma = 0
    media = 0
    print(f"Os termos da sequência aritmética, dados os números {a} como primeiro termo, {r} como razão e {n} como termo máximo são: ", end="")
    for i in range(a, n, r):
        print(i, end=" ")
        soma += i
        media += i
    media = media / n
    print(f"""
    Soma dos termos: {soma}
    Média dos termos: {media}
    """)


def main():
    limpar_tela()
    while True:
        a, r, n = obter_termos()
        exibir_progressao_arit(a, r, n)
        print("""Deseja calcular outra progressão? 
        1 - Sim
        2 - Não""")
        continuar = obter_inteiro()
        if continuar == 2:
            break


main()