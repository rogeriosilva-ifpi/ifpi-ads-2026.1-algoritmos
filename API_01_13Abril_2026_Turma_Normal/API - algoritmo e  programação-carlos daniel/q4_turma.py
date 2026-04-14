def analisar_turma():
    n = int(input("Quantos alunos tem na turma? "))
    soma_notas = 0
    aprovados = 0
    reprovados = 0
    
    primeira_nota = float(input("Digite a nota do aluno 1 (0 a 10): "))
    while primeira_nota < 0 or primeira_nota > 10:
        primeira_nota = float(input("Nota inválida! Digite entre 0 e 10: "))
    
    maior_nota = primeira_nota
    menor_nota = primeira_nota
    soma_notas = primeira_nota
    
    if primeira_nota >= 7:
        aprovados = aprovados + 1
    elif primeira_nota < 5:
        reprovados = reprovados + 1
        
    for i in range(2, n + 1):
        nota = float(input(f"Digite a nota do aluno {i} (0 a 10): "))
        
        while nota < 0 or nota > 10:
            nota = float(input("Nota inválida! Digite entre 0 e 10: "))
            
        soma_notas = soma_notas + nota
        
        if nota > maior_nota:
            maior_nota = nota
        
        if nota < menor_nota:
            menor_nota = nota
            
        if nota >= 7:
            aprovados = aprovados + 1
        elif nota < 5:
            reprovados = reprovados + 1

    media = soma_notas / n
    
    print("\n--- RESULTADOS ---")
    print("Maior nota:", maior_nota)
    print("Menor nota:", menor_nota)
    print(f"Média da turma: {media:.2f}")
    print("Quantidade de Aprovados:", aprovados)
    print("Quantidade de Reprovados:", reprovados)

analisar_turma()