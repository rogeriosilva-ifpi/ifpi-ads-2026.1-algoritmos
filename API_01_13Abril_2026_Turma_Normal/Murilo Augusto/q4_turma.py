def main():
    
    numero_notas = int(input("Escolha quantas notas deseja processar: "))
    for i in range(numero_notas):
        Aluno = input("Nome do aluno: ")
        nota = int(input("Nota: "))
        if nota >= 7:
            print("aprovado")
        elif nota  >= 5 < 7: 
            print("recuperação")
        elif nota < 5:
            print("reprovado")

    for a in range(i):
        print(a)
        

main()