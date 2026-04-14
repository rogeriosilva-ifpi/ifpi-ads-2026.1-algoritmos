def main():
    while True:
        senha = int(input("Senha: "))
        digito_1 = senha // 100000
        digito_2 = (senha % 100000) // 10000
        digito_3 = ((senha % 100000) % 10000) // 1000
        digito_4 = (((senha % 100000) % 10000) % 1000) // 100
        digito_5 = ((((senha % 100000) % 10000) % 1000) % 100) // 10
        digito_6 = ((((senha % 100000) % 10000) % 1000) % 100) % 10
        soma = digito_1 + digito_2 + digito_3 + digito_4 + digito_5 + digito_6
        if digito_2 == digito_1+1 or digito_3 == digito_2+1 or digito_4 == digito_3+1 or digito_5 == digito_4+1 or digito_6 == digito_5+1:
            print("Senha Inválida: Não podem haver dois dígitos iguais consecutivos")
        elif soma <= 20:
            print("Senha Inválida: A soma dos dígitos não pode ser menor do que 20")
        elif digito_1 == 0:
            print("Senha Inválida: O primeiro dígito não pode ser zero")
        else: 
            print("Senha Válida")
            break
        
    

main()