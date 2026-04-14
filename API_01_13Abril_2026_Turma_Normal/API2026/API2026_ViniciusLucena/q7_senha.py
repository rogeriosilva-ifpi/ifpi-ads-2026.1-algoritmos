def main():
    while True:
        senha = input("digite uma senha de 6 digitos: ")

        #primeira regra: tamanho
        if len(senha) != 6:
            print("digite uma senha com 6 caracteres")
            continue

        #regra 2: não pode começar com 0
        if senha(0) == 0:
            print("senha inválida")
            continue

        #regra 3: só números
        if not senha.isdigit():
            print("senha inválida")
            continue

        if validar(senha):
            break
        else:
            print("senha inválida")
    print("senha inválida")


def validar(s):
    soma=0

    for i in range(6):
        soma += int(s[i])

        if i < 5 and s[i] == s[i+1]:
            return False
        

    if soma <=20:
        return False
    
    return True






main()