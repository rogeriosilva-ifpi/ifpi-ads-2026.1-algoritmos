def calcular_pa():
    continuar = 'S'
    
    while continuar == 'S' or continuar == 's':
        a = float(input("Digite o primeiro termo: "))
        r = float(input("Digite a razão: "))
        n = int(input("Digite o número de termos (n >= 2): "))
        
        while n < 2:
            n = int(input("Erro! Digite um n maior ou igual a 2: "))
            
        soma = 0
        termo = a
        
        print("Sequência:", end=" ")
        for i in range(n):
            print(termo, end=" ")
            soma = soma + termo
            termo = termo + r
            
        media = soma / n
        print("\nSoma total:", soma)
        print("Média dos termos:", media)
        
        continuar = input("\nDeseja calcular outra P.A.? (S/N): ")

calcular_pa()