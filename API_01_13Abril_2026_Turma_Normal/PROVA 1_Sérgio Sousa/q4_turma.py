def final(nota):
    if nota < 5.0:
        return "Reprovado"
    elif nota < 7.0:
        return "Recuperação"
    elif nota >= 7.0:
        return "Aprovado"
    else:
        return "Reprovado"

def main():
    for i in range(10):
        while True:
            try:
                nota = float(input(f"Aluno {i+1} - Nota: "))
                break
            except ValueError:
                print("Erro: Digite um número válido!")
        resultado = final(nota)
        print(f"Aluno {i+1}: {resultado}")

main()