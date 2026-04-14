def main():
    N = int(input("Número de Alunos: "))
    maior_nota = 0
    menor_nota = 0
    soma = 0
    aprovados = 0
    reprovados = 0
    recuperacao = 0
    for i in range(1, N+1):
        nota = int(input(f"Digite a nota do aluno Nº{i}: "))

        soma += nota

        if nota == 0 or nota > maior_nota:
            maior_nota = nota
        elif nota == 0 or nota < menor_nota:
            menor_nota = nota

        if nota >= 7:
            aprovados += 1
            print("Aprovado")
        elif nota >= 5:
            recuperacao += 1
            print("Recuperação")
        else:
            reprovados += 1
            print("Reprovado")
    
    media = soma / N
    print(f"Maior nota: {maior_nota}")
    print(f"Menor nota: {menor_nota}")
    print(f"Média da turma: {media}")
    print(f"Número de Aprovados: {aprovados}, Número de Reprovados: {reprovados}, Alunos em Recuperação: {recuperacao}")

main()