def main():
    N = obter_int_pos()
    calcular_divisores(N)



def obter_int_pos(instrucoes : str = "Digite um inteiro positivo: "):
    inteiro = int(input(instrucoes))
    if inteiro > 0:
        return inteiro

def calcular_divisores(numero):
    n_divisores = 0
    print(f"Divisores de {numero}:")
    for i in range(1, numero+1):
        if numero % i == 0:
            n_divisores += 1
            print(i, end = " ")
    print()
    print(f"{numero} tem {n_divisores} divisores")



main()