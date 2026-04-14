def main():
    N = int(input("Digite N: "))
    M = int(input("Digite M: "))
    intervalo(N,M)


def intervalo(N, M): 
    if N < M:
        qtd = 0
        soma = 0
        for i in range(N, M + 1):
            if i % 2 != 0 and i % 3 == 0:
                soma += i
                qtd += 1
                print(i, end = " ")
        if qtd > 0:
            print(f"Soma: {soma}")
        elif qtd == 0:
            print("Não foram encontrados números que satisfazessem a condição")

        
main()