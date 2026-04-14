import os
from utils.os_utils import limpar_tela
from utils.number_utils import obter_inteiro


def obter_senha():
    print("Insira uma senha de exatamente 6 dígitos: ", end="")
    senha = obter_inteiro()
    while len(str(senha)) > 6 or len(str(senha)) < 6:
        print("Tamanho inválido, insira outra senha: ", end="")
        senha = obter_inteiro()
        soma_digitos, dig_1, digitos_iguais = somar_digitos(senha)
    soma_digitos, dig_1, digitos_iguais = somar_digitos(senha)
    while digitos_iguais == True:
        print("A senha não pode ter dois dígitos iguais consecutivos, tente novamente: ", end="")
        senha = obter_inteiro()
        soma_digitos, dig_1, digitos_iguais = somar_digitos(senha)        
    while soma_digitos > 20:
        print("A soma dos dígitos não deve ser maior que 20, tente novamente: ", end="")
        senha = obter_inteiro()
        soma_digitos, dig_1, digitos_iguais = somar_digitos(senha)
    while dig_1 == 0:
        print("O primeiro dígito não pode ser 0. Tente novamente: ", end="")
        senha = obter_inteiro()
        soma_digitos, dig_1, digitos_iguais = somar_digitos(senha)
    return senha


def somar_digitos(senha):
    digitos_iguais = False
    dig_1 = senha // 100000
    dig_2 = senha // 10000 - dig_1 * 10
    dig_3 = senha // 1000 - (dig_2 * 10 + dig_1 * 100)
    dig_4 = senha // 100 - (dig_3 * 10 + dig_2 * 100 + dig_1 * 1000)
    dig_5 = senha // 10 - (dig_4 * 10 + dig_3 * 100 + dig_2 * 1000 + dig_1 * 10000)
    dig_6 = senha - (dig_5 * 10 + dig_4 * 100 + dig_3 * 1000 + dig_2 * 10000 + dig_1 * 100000)
    soma_digitos = dig_1 + dig_2 + dig_3 + dig_4 + dig_5 + dig_6
    if dig_1 == dig_2 or dig_2 == dig_3 or dig_3 == dig_4 or dig_4 == dig_5 or dig_5 == dig_6:
        digitos_iguais = True
    return soma_digitos, dig_1, digitos_iguais
    

def main():
    limpar_tela()
    senha = obter_senha()
    print("Senha válida. Cadastro validado.")


main()