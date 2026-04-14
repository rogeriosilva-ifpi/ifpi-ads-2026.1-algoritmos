def divisores(n):

    contador = n
    qt_divisores = 0
    while contador > 0:
        teste = n % contador 
        if  teste == 0:
            print(n // contador)
            qt_divisores += 1
        contador -= 1

    return(f"Total: {qt_divisores} divisores.") 
        

def main():
    num = int(input("Digite um número: "))
    res = divisores(num)

    print(res)
if __name__ == "__main__":
    main()
