from utils import *

def main():
    primeiro_termo = obter_inteiro('primeiro termo: ')
    razao = obter_inteiro('Razão: ')
    numero_termos = obter_inteiro('Número de termos: ')
    
    termos = ''
    termos += str(primeiro_termo) + ' '
    termo = primeiro_termo
    
    while numero_termos > 1:
        termo = termo * 2
        termos = termos + str(termo) + ' '
        numero_termos -= 1
        
    print(termos)
    
    
main()