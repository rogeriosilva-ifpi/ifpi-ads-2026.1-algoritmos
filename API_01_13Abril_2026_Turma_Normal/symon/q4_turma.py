def avaliar(n):

    qt_aprovados = 0
    qt_reprovados = 0
    qt_recuperacao = 0
    soma = 0
    for i in range(n-1):
        nota = float(input("Digite a nota do aluno: "))
        if nota >= 0 and nota <= 10:
            if nota < 5:
                print("Aluno reprovado.")
                qt_reprovados +=1
            elif nota >= 5 and nota < 7:
                print("Aluno de recuperação")
                qt_recuperacao += 1
            else:
                print("Aluno Aprovado.")
                qt_aprovados += 1
            soma += nota

            menor_nota = nota
            maior_nota = nota

            if nota <= menor_nota:
                menor_nota = nota   
            if nota >= maior_nota:
                maior_nota = nota

    media = soma / n

    return f"Maior nota: {maior_nota:.2f}, Menor nota: {menor_nota:.2f}, Média da turma: {media:.2f}, Alunos aprovados: {qt_aprovados}, Alunos de recuperação: {qt_recuperacao}, Alunos reprovados: {qt_reprovados}"

def main():
    qt_alunos = int(input("Digite a quantidade de alunos: "))
    res = avaliar(qt_alunos)
    print(res)

if __name__ == "__main__":
    main()