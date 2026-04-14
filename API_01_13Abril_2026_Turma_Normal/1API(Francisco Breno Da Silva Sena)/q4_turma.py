def main():
    n = int(input("Digite a quantidade de alunos:"))
    contador = 0
    aprovados = 0
    recuperacao = 0
    reprovados = 0
    maior = 0
    notas_total = 0
    soma = 0

    while contador < n:
        nota = float(input("Digite a nota do aluno.( Entre 0 e 10)"))
        soma += nota
        if nota >= 7:
            print("Aprovado!")
            aprovados += 1
        elif nota >= 5:
            print("Está de recuperação!")
            recuperacao += 1
        else:
            print("Reprovado!")
            reprovados += 1

        if contador == 0:
            maior = nota
            menor = nota

        else:
            if nota > maior:
                maior = nota
            
            if nota < menor:
                menor = nota
        
        notas_total += 1
        contador += 1
        
    media = soma / notas_total
    print(f"A maior nota é: {maior}")
    print(f"A menor nota é: {menor}")
    print(f"Quantidade de alunos em situação Aprovados: {aprovados}")
    print(f"Quantidade de alunos em situação Recuperação: {recuperacao}")
    print(f"Quantidade de alunos em situação Reprovados: {reprovados}")
    print(f"média das notas dos alunos: {media:.1f}")













main()