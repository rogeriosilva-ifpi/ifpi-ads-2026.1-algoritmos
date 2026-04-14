def main():
    mostrar_situacao()

def mostrar_situacao():
    n = int(input())
    for i in range(n):
        notas = float(input('Digite a nota do aluno: '))
        
        if notas >= 7:
            print('Aprovado!')
        if 5 <= notas < 7:
            print('Recuperaçâo!')
        if notas < 5:
            print('Reprovado!')
            
    maior_nota = notas > notas 
    menor_nota = notas < notas
    print(maior_nota)
    print(menor_nota)
    
main()