def escala():
    print(" 0 = Nunca\n 1 = Raramente\n 2 = Às vezes\n 3 = Regularmente\n 4 = Frequentemente\n 5 = Quase sempre\n 6 = Sempre")

def obter_resposta():
    pessoa = input(print("Informe seu nome: "))
    float dimensao_um = 0
    float dimensao_dois = 0
    float dimensao_tres = 0
    
    # Dimensão 1
    
    dimensao_um += input(print("Sinto-me emocionalmente esgotado(a) pelos meus estudos/trabalho(1 a 6)"))
    dimensao_um += input(print("Sinto-me esgotado (a) ao final de um dia de estudo/trabalho(1 a 6)"))
    dimensao_um += input(print("Acordar de manhã e ter que enfrentar mais um dia me causa cansaço(1 a 6)"))
    # Despersonalizacao
    dimensao_dois += print("Sinto que me tornei mais indiferente com as pessoas ao meu redor(1 a 6)")
    dimensao_dois += print("Tenho me preocupado menos com o impacto do meu trabalho/estudo nas pessoas(1 a 6)")
    dimensao_dois += print("Sinto que as pessoas ao meu redor me culpam por alguns dos seus problemas(1 a 6)")
    # Realizacao pessoal
    dimensao_tres += print("Consigo lidar eficazmente com os problemas que surgem no meu dia a dia(1 a 6)")
    dimensao_tres += print("Sinto que estou tendo uma influencia positiva na vida das pessoas(1 a 6)")
    dimensao_tres += print("Sinto-me estimulado(a) após trabalhar ou estudar com outras pessoas(1 a 6)")

def calcular_escores(dimensao):
    media = dimensao/3;
    return media

def classificar_dimensao(media):
    baixo = 1
    moderado = 2
    alto = 3
    
    if(media < 0.0 or media > 2.0):
        baixo = true
        return baixo
        break
    else(media < 2.1 or media > 3.9):
        moderado = true
        return media
        break   
    elif(media < 4.0 or media > 6,0):
        alto = true
        return alto
        break   
    

def exibir_laudo():
    print("LAUDO")
    print(f"Exaustao")

def main():

    int(input(print(f"Informe o número de pessoas que irão participar do estudo:")))
    return 0

main()
