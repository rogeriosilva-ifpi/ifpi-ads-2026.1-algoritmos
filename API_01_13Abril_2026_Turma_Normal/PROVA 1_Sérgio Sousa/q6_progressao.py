while True:
    a = float(input("Primeiro termo: "))
    r = float(input("Razão: "))
    n = int(input("Número de termos: "))
    
    while n < 2:
        n = int(input("Número de termos deve ser no mínimo 2: "))
    
    soma = 0
    print("Termos da sequência:")
    for i in range(n):
        termo = a + (i * r)
        soma += termo
        print(termo)
    
    print(f"Soma: {soma}")
    
    media = soma / n
    print(f"Média: {media}")
    
    continuar = input("Deseja calcular mais uma vez? (s/n): ")
    if continuar.lower() != 's':
        break
