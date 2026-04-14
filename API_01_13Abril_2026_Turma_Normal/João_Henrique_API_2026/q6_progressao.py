def main():
    while True:
        a = int(input("Primeiro Termo: "))
        r = int(input("Razão: "))
        n = int(input("Número de Termos: "))
        soma_total = 0
        qtd = 0
        if n >= 2:
            for i in range(a, n+1, r):
                soma_total += i
                qtd += 1
                print(i, end = " ")
        media = soma_total / qtd
        print()
        print(f"Soma dos Termos: {soma_total}")
        print(f"Média dos Termos: {media}")
        pergunta = input("Você deseja calcular outra progressão? (Responda com sim ou não)")
        if pergunta == "não":
            break
        

main()