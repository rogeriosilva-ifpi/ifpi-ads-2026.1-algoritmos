def main():
    primeiro_termo = int(input("Digite o primeiro termo: "))
    razão = int(input("Digite a razão da progressão: "))
    termos = int(input("Digite o número de termos que vai ter: "))
     

    if termos < 2:
        print("A quantidade de termos da sua progressão tem que ser no minimo 2!")
    else:
        for termos in range (primeiro_termo, termos + 1, razão):
            
            print(termos) 
            
main()

#funciona se o primeiro termo e a razão forem 1