def obter_inteiro(conteudo = 'Digite um número inteiro: '):
    while True:
        try:
            inteiro = int(input(conteudo))
            return inteiro
        except:
            print('Valor inválido')
            
            
            
def obter_inteiro_positivo(conteudo = 'Digite um número inteiro: '):
    while True:
        try:
            inteiro = int(input(conteudo))
            if inteiro > -1:
                return inteiro
            erro = 1 / 0
        except:
            print('Valor inválido')
            
            
            
def obter_real(conteudo = 'Digite um número real: '):
    while True:
        try:
            real = float(input(conteudo))
            return real
        except:
            print('Valor inválido')
            

def obter_real_minimo(conteudo, inferior):
    while True:
        try:
            real = float(input(conteudo))
            if real >= inferior:
                return real
            erro = 1 / 0
        except:
            print('Valor inválido') 
            
            
def obter_real_intervalo(conteudo, inferior, superior):
    while True:
        try:
            real = float(input(conteudo))
            if real >= inferior and real <= superior:
                return real
            erro = 1 / 0
        except:
            print('Valor inválido')
            

def obter_inteiro_intervalo(conteudo, inferior, superior):
    while True:
        try:
            inteiro = float(input(conteudo))
            if inteiro >= inferior and inteiro <= superior:
                return inteiro
            erro = 1 / 0
        except:
            print('Valor inválido')