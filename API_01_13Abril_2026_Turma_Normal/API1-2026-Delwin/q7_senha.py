from utils import obterInteiro

def Main():
    #Pedindo a senha a ser validada, verificando a quantidade de dígitos
    senha = input('Digite a senha (Apenas dígitos numéricos): ')

    while len((senha)) != 6:
        senha = input('Digite a senha (Apenas dígitos numéricos): ')

    #Validando a senha
    if validaSenha(senha) == True:
        print(f'A senha {senha} é válida!!!')
    else:
        print(f'A senha {senha} é inválida!!!')


def validaSenha(senha):
    #Recebe uma senha e verifica se é válida (true) ou não (falsa)
    senha = str(senha)
    n = 0
    soma = 0
    if senha[0] == '0':
        print('Não pode começar com 0!')
        return False
    for i in senha:
        if i == n:
            print('Não pode haver dois dígitos iguais em sequência!')
            return False
        soma += int(i)
        n == i
    if soma <= 20:
        print('A soma dos dígitos precisa ser maior que 20!')
        return False
    return True


Main()