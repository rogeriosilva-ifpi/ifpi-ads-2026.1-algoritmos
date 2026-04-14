def main():

    

    a = int(input("Digite o primeiro termo: "))
    r = int(input("Digite a razão: "))
    n = int(input("Digite o número de termos: "))
    
    soma = 0

    if n < 2:
        print("Digite um número a partir de 2.")
          

        for i in range(a, n + 1, r):
            
            soma += i
            media = soma / n

            print(i)
            
        print(f"Soma: {soma}")
        print(f"Média: {media}")

   





main()