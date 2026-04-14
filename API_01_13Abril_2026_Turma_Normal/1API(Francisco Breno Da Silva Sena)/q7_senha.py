def main():

    valida = False
    while valida == False:
        def consecutivos(s):
            cent_milhar = s // 100000
            dez_milhar = (s // 10000) % 10
            uni_milhar = ((s // 1000) % 100) % 10
            centena = (((s // 100) % 1000) % 100) % 10
            dezena =  (s // 10) % 10
            unidade = s % 10

            if cent_milhar == dez_milhar:
                return False
            if dez_milhar == uni_milhar:
                return False
            if uni_milhar == centena:
                return False
            if centena == dezena:
                return False
            if dezena == unidade:
                return False
            


        def p_digito(senha):
            cent_milhar = senha // 100000
            if cent_milhar == 0:
                return False
            


        def soma(s):
            cent_milhar = s // 100000
            dez_milhar = (s // 10000) % 10
            uni_milhar = ((s // 1000) % 100) % 10
            centena = (((s // 100) % 1000) % 100) % 10
            dezena =  (s // 10) % 10
            unidade = s % 10
            soma = cent_milhar + dez_milhar + uni_milhar + centena + dezena + unidade
            if soma < 20:
                return False
            


        senha = int(input("Digite a senha de 6 dígitos:"))
        validar_consecutivos = consecutivos(senha)
        validar_primeiro_dig = p_digito(senha)
        validar_soma = soma(senha)
        if validar_consecutivos == False:
            print(f"Vocẽ digitou um mesmo nṹmero consecutivo!")
            valida = False
            print("Tente Novamente!")
        elif validar_primeiro_dig == False:
            print(f"Você digitou o primeiro dígito como 0!")
            valida = False
            print("Tente Novamente!")
        elif validar_soma == False:
            print(f"Você digitou uma senha cuja soma dos algarismos é menor que 20!")
            valida = False
            print("Tente Novamente!")
        else:
            valida = True
            

    senha_definida = senha
    print(f"Sua senha definida é {senha_definida}")
    










   



















main()