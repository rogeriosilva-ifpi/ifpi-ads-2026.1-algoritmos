def main():
    n = int(input())
    m = int(input())

    if n >= m:
        print("n deve ser menor que m")
        return

    soma = 0
    encontrou = False
    for i in range(n + 1, m):
        if i % 3 == 0 and i % 2 != 0:
            print(i)
            soma += i
            encontrou = True
    
    if encontrou:
        print(f"Soma: {soma}")
    else:
        print("Nenhum número satisfaz a condição")
           
main()