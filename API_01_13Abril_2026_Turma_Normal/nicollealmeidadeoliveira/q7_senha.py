from utils import obter_texto

def main():
    while True:
        senha = obter_texto('Crie uma senha de no mínimo 6 dígitos: ')
        if len(senha) < 6:
            continue
        break

    valida = validar_senha(senha)
    





def validar_senha():
    

