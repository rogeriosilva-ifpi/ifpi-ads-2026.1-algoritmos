def validar_senha():
    cadastrou = False
    
    while cadastrou == False:
        senha = input("Cadastre uma senha de 6 dígitos: ")
        
        if len(senha) != 6:
            print("Erro: A senha deve ter exatamente 6 dígitos!")
        elif senha[0] == '0':
            print("Erro: O primeiro dígito não pode ser zero!")
        else:
            soma = 0
            repetido = False
            
            for i in range(6):
                soma = soma + int(senha[i])
                
                if i < 5:
                    if senha[i] == senha[i+1]:
                        repetido = True
            
            if repetido == True:
                print("Erro: Não pode ter dígitos iguais consecutivos!")
            elif soma <= 20:
                print("Erro: A soma dos dígitos deve ser maior que 20!")
            else:
                confirmar = input("Confirme a senha: ")
                if confirmar == senha:
                    print("Senha cadastrada!")
                    cadastrou = True
                else:
                    print("As senhas não batem!")
validar_senha()