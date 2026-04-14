def validar_senha(senha):
    try:
        if len(senha) != 6:
            return False
        
        if senha[0] < '1' or senha[0] > '9':
            return False
        
        soma = 0
        for c in senha:
            if c < '0' or c > '9':
                return False
            soma += int(c)
        
        if soma <= 20:
            return False
        
        for i in range(len(senha) - 1):
            if senha[i] == senha[i + 1]:
                return False
        
        return True
    
    except:
        return False


senha = input("Digite uma senha: ")
if validar_senha(senha):
    print("Senha válida!")
else:
    print("Senha inválida!")

