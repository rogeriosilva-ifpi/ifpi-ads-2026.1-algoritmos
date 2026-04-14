def obterInteiro(label):
    #Recebe uma string como parâmetro e retorna um número inteiro.
    while True:
        try:
            return int(input(label))
            break
        except:
            print('Valor inválido!')


def obterPorcentagem(label):
    #Recebe uma string como parâmetro e retorna um número float representando uma porcentagem.
    while True:
        try:
            return (float(input(label))/100)
            break
        except:
            print('Valor inválido!')


def obterFloat(label):
    #Recebe uma string como parâmetro e retorna um número float.
    while True:
        try:
            return float(input(label))
            break
        except:
            print('Valor inválido!')


def confirma(label):
    #Recebe sim ou não e retorna um booleano
    #Tudo o que não for interpretado como sim será tratado como não
    entrada = ''
    while True:
        try:
            entrada = input(label)
            break
        except:
            print('Valor inválido!')

    if entrada == 's' or entrada == 'S' or entrada == 'Sim' or entrada == 'sim' or entrada == 'SIM':
        return True
    else:
        return False