def main():
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    nulo = 0
    branco = 0
    voto = 0
    somatorio = 0
    opcao = int(input(menu()))

    while opcao != 3:
        if opcao == 1:
            voto = int(input(votar()))
            if voto != 5 and voto != 0:
                somatorio += 1


            if voto == 1:
                c1 += 1
            elif voto == 2:
                c2 += 1
            elif voto == 3:
                c3 += 1
            elif voto == 4:
                c4 += 1
            elif voto == 5:
                nulo += 1
            else:
                branco += 1



        else:
            print(ver_resultado(c1, c2, c3, c4, nulo, branco, somatorio))

        opcao = int(input(menu()))
    print(ver_resultado(c1, c2, c3, c4, nulo, branco, somatorio))
    ganhador(c1, c2, c3, c4, somatorio)

def ganhador(c1, c2, c3, c4, s):
    pc1 = c1 / s
    pc2 = c2 / s
    pc3 = c3 / s
    pc4 = c4 / s
    if pc1 < 0.5 and pc2 < 0.5 and pc3 < 0.5 and pc4 < 0.5:
        return print('Haverá um Segundo turno.')
    else:
        if c1 > c2 and c1 > c3 and c1 > c4:
            return print('Candidato 1 é o vencedor.')
        elif c2 > c1 and c2 > c3 and c2 > c4:
            return print('Candidato 2 é o vencedor.')
        elif c3 > c1 and c3 > c2 and c3 > c4:
            return print('Candidato 3 é o vencedor.')
        else:
            return print('Candidato 4 é o vencedor.')

            
    




def ver_resultado(c1, c2, c3, c4, n, b, s):

    return f'''
candidato 1: {c1}, %: {((c1 / s) * 100):.2f}
candidato 2: {c2}, %: {((c2 / s) * 100):.2f}
candidato 3: {c3}, %: {((c3 / s) * 100):.2f}
candidato 4: {c4}, %: {((c4 / s) * 100):.2f}
Nulo: {n}
branco:{b}'''


def menu():
    return '''
1 - Votar
2 - Ver Resultado
3 - Encerrar
: '''

def votar():
    return '''
1 - Candidato 1
2 - Candidato 2
3 - candidato 3
4 - Candidato 4
5 - Nulo
0 - Branco
: '''

main()