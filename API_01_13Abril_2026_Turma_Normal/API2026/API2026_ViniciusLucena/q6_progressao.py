def main():
    while True:
        a = float(input("digite o primeiro termo: "))
        r = float(input("digite a razão: "))
        n = int(input("digite o núimero de termos: "))

        calcular(a, r, n)

        op = input("deseja continuar? se sim, digite s: ")
        if op != s:
            break



def calcular(a, r, n):
    termo=a
    soma=0

    for i in range(n):
        print(termo)
        soma += termo
        termo += r

    media = soma / n

    print ("a soma é: ", soma)
    print ("a média é: ", media)







main()
