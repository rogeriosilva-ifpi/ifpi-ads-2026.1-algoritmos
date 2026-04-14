def main():
    n1 = float(input('Informe a nota do aluno 1:  '))
    n2 = float(input('Informe a nota do aluno 2:  '))
    n3 = float(input('Informe a nota do aluno 3:  '))
    n4 = float(input('Informe a nota do aluno 4:  '))
    n5 = float(input('Informe a nota do aluno 5:  '))
    n6 = float(input('Informe a nota do aluno 6:  '))
    n7 = float(input('Informe a nota do aluno 7:  '))
    n8 = float(input('Informe a nota do aluno 8:  '))
    n9 = float(input('Informe a nota do aluno 9:  '))
    n10 = float(input('Informe a nota do aluno 10:  '))

    lista = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]
    maximo = max(lista)
    minimo = min(lista)
    med = (n1+n2+n3+n4+n5+n6+n7+n8+n9+n10)/10

    print(f'Maior nota: {maximo}')
    print(f'Menor nota: {minimo}')
    print(f'Media: {med}')

    if n1 >= 7:
        print('Aluno 1 Aprovado')
    elif n1 >= 5:
        print('Aluno 1 Recuperação')
    else:
        print('Aluno 1 Reprovado')
    
    if n2 >= 7:
        print('Aluno 2 Aprovado')
    elif n2 >= 5:
        print('Aluno 2 Recuperação')
    else:
        print('Aluno 2 Reprovado')
    
    if n3 >= 7:
        print('Aluno 3 Aprovado')
    elif n3 >= 5:
        print('Aluno 3 Recuperação')
    else:
        print('Aluno 3 Reprovado')
    
    if n4 >= 7:
        print('Aluno 4 Aprovado')
    elif n4 >= 5:
        print('Aluno 4 Recuperação')
    else:
        print('Aluno 4 Reprovado')
    
    if n5 >= 7:
        print('Aluno 5 Aprovado')
    elif n5 >= 5:
        print('Aluno 5 Recuperação')
    else:
        print('Aluno 5 Reprovado')
    
    if n6 >= 7:
        print('Aluno 6 Aprovado')
    elif n6 >= 5:
        print('Aluno 6 Recuperação')
    else:
        print('Aluno 6 Reprovado')
    
    if n7 >= 7:
        print('Aluno 7 Aprovado')
    elif n7 >= 5:
        print('Aluno 7 Recuperação')
    else:
        print('Aluno 7 Reprovado')
    
    if n8 >= 7:
        print('Aluno 8 Aprovado')
    elif n8 >= 5:
        print('Aluno 8 Recuperação')
    else:
        print('Aluno 8 Reprovado')
    
    if n9 >= 7:
        print('Aluno 9 Aprovado')
    elif n9 >= 5:
        print('Aluno 9 Recuperação')
    else:
        print('Aluno 9 Reprovado')
    
    if n10 >= 7:
        print('Aluno 10 Aprovado')
    elif n10 >= 5:
        print('Aluno 10 Recuperação')
    else:
        print('Aluno 10 Reprovado')





main()