
def main():
    M = int(input("Insira o maior valor: "))    
    N = int(input("Insira o menor valor: "))

    print("Números: ", end=" ")
    for i in range (N, M):
        if (i % 3 == 0):
                for j in range (1, i+1):
                    if (i / 3 == j * 3):
                        print(i, end=" ")
main()
