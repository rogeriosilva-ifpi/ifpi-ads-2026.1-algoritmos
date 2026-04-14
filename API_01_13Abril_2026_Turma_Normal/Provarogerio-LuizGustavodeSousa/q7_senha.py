def main():

    senha = input('Digite uma senha de seis dígitos: ')

    
    repetido = False
    for i in range(len(senha) - 1):
        if senha[1] == senha[i+1]:
            repetido = True
            break

    if len(senha) != 6 or not ():
        print('Dever conter 6 dígitos.')
        
        
    elif senha [0] == 0:
        print('O primeiro digito dever difente de zero.')


    elif repetido:
        print('A senha não dever conter digitos iguais em sequência.')


main()