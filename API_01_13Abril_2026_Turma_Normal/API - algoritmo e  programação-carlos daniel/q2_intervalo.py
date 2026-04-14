def analisar_intervalo():

    n = int(input("Digite o valor de N: "))
    m = int(input("Digite o valor de M (maior que N): "))

    if m <= n:
        print("Erro: M deve ser obrigatoriamente maior que N!")
    else:
        soma = 0
        quantidade = 0 
        
        print(f"Números ímpares e divisíveis por 3 entre {n} e {m}:")
        
        for i in range(n, m + 1):
            if i % 2 != 0 and i % 3 == 0:
                print(i, end=" ")
                soma = soma + i
                quantidade = quantidade + 1
        
        if quantidade > 0:
            print(f"\nA soma desses números é: {soma}")
        else:
            print("\nNenhum número satisfaz a condição neste intervalo.")
analisar_intervalo()