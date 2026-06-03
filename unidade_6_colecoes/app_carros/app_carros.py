import os

def main():
    carros = []
    limpar_tela()
    menu = '''
    >>> App Carros <<<
    1 - Novo Carro
    2 - Listar Carros
    3 - Listar carros ordenados pelo nome
    4 - Buscar por nome

    0 - Sair > '''

    opcao = int(input(menu))

    while opcao != 0:

        if opcao == 1:
            limpar_tela()
            print('> Adicionando novo carro')
            nome = input('Nome: ')
            ano = int(input('Ano: '))
            preco = float(input('Preço: '))
            novo_carro = {'nome': nome, 'ano': ano, 'preco': preco}
            carros.append(novo_carro)
            sucesso()
        elif opcao == 2:
            limpar_tela()
            listar_carros(carros)
        elif opcao == 3:
            carros_ordenados = sorted(carros, key=por_nome)
            listar_carros(carros_ordenados)
        elif opcao == 4:
            limpar_tela()
            print('Pesquisa de carros:')
            texto =  input('Nome ou parte: ')
            carros_encontrados = filtrar_por_parte_nome(carros, texto)
            listar_carros(carros_encontrados)
            

        input('Enter to continue...')
        limpar_tela()
        opcao = int(input(menu))


def por_nome(carro):
    return carro['nome']



def listar_carros(carros):
    print(f'{len(carros)} carros cadastrados')
    for carro in carros:
        print('>', carro['nome'], carro['ano'], carro['preco'])
        
    print(20*'-')    
    sucesso()


def filtrar_por_parte_nome(carros, texto):
    cestinha = []

    for carro in carros:
        if texto.upper() in carro['nome'].upper():
            cestinha.append(carro)
    
    return cestinha


def limpar_tela():
    os.system('clear')


def sucesso():
    print('Operacao realizada com sucesso!')


main()