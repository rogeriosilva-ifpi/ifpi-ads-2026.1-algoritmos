def main():
    menu()
    opcao = int(input())

    voto0 = 0
    voto1 = 0
    voto2 = 0
    voto3 = 0
    voto4 = 0
    voto5 = 0
    while opcao != 3:
        if opcao == 1:
            voto = int(input('Qual candidato deseja votar?(0 - branco, 1, 2, 3, 4 ou 5 - nulo) '))
            if voto == 0:
                voto0 += 1
            elif voto == 1:
                voto1 += 1
            elif voto == 2:
                voto2 += 1
            elif voto == 3:
                voto3 += 1
            elif voto == 4:
                voto4 += 1
            elif voto == 5:
                voto5 += 1

    vencedor = vencedor(voto1, voto2, voto3, voto4)
def vencedor(voto1, voto2, voto3, voto4):
    mais_votos = max(voto1, voto2, voto3, voto4)
    if mais_votos == voto1:
        return 'Candidato 1'
    elif mais_votos == voto2:
        return 'Candidato 2'
    elif mais_votos == voto3:
        return 'Candidato 3'
    elif mais_votos == voto4:
        return 'Candidato 4'
    else:
        return 'Empate'
    

def percentual(voto1, voto2, voto3, voto4):
    ...

   
def menu():
    menu = '''
    1 - Votar
    2 - Ver Resultado
    3 - Encerrar
'''
    print(menu)

def tela(voto0, voto1, voto2, voto3, voto4, voto5, ):
    totais_validos = voto1 + voto2 + voto3 + voto4
    tela = f'''
    Total de votos válidos: {totais_validos}
    Total de votos brancos: {voto0}
    Total de votos nulos: {voto5}
    Percentual Candidato 1: {}%
    Percentual Candidato 2: {}%
    Percentual Candidato 3: {}%
    Percentual Candidato 4: {}%
'''
    print(tela)

main()