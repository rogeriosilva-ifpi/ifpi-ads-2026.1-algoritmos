from utils import *

def main():
    contador = obter_inteiro_positivo('Quantos pacientes? ')
    
    while contador > 0:
        contador -= 1
        nome = input('Nome: ')
        score1 = obter_respostas()
        dimensao1 = classificar_dimensao(score1)
        exibir_laudo(nome, score1, dimensao1)
    
    
def obter_respostas():
    resposta_1 = obter_inteiro_intervalo("Sinto-me emocionalmente esgotado(a) pelos meus estudos/trabalho(0-6): ", 0, 6)
    resposta_2 = obter_inteiro_intervalo("Sinto-me esgotado(a) ao final de um dia de estudos/trabalho(0-6): ", 0, 6)
    resposta_3 = obter_inteiro_intervalo("Acordar de manhã e ter que enfrentar mais um dia me causa cansaço: ", 0, 6)
    score1 = calcular_score(resposta_1, resposta_2, resposta_3)
    return score1
    
    
def calcular_score(r1, r2, r3):
    return (r1 + r2 + r3) / 3


def classificar_dimensao(s1):
    if s1 > 3.9:
        return 'Alto'
    elif s1 > 2:
        return 'Moderado'
    else:
        return 'Baixo'
    
    
def exibir_laudo(n, s, d):
    print(f'''
--- LAUDO: {n} ---
Exaustão emocional: {s} --> {d}''')
    
    
main()