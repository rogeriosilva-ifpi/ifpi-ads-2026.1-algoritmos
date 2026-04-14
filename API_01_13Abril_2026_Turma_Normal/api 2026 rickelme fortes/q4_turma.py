def main():

    N = int(input("Digite o número de alunos (0 a 10): "))

    maior_nota = 0
    menor_nota = 0
    media_turma = 0

    aluno_aprovado = 0
    aluno_recuperar = 0
    aluno_reprovado = 0

    if N > 10 and N < 0:
        print("Digite um número válido.")

    else:

     for i in range(N):
         nota = int(input("Digite a nota do aluno (0 a 10): "))
        
         if nota >= 7:
            aluno_aprovado += 1
            print("Aprovado")

         if nota >= 5 and nota < 7:
            aluno_recuperar += 1
            print("Recuperação")

         if nota < 5:
            aluno_reprovado += 1
            print("Reprovado")
        
     soma += nota

     maior_nota = nota
     menor_nota = nota

     if menor_nota > maior_nota:
            maior_nota = menor_nota
        
     if maior_nota < menor_nota:
            menor_nota = maior_nota


     calculo_media = soma / N
     media_turma == calculo_media

     print(f"Maior nota: {maior_nota}")
     print(f"Menor nota: {menor_nota}")
     print(f"Alunos aprovados: {aluno_aprovado}")
     print(f"Alunos em recuperação: {aluno_recuperar}")
     print(f"Alunos reprovados: {aluno_reprovado}")
     print(f"Média da turma: {media_turma}")

    




main()