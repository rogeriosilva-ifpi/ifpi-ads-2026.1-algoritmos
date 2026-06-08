import os

def main():
    carros = load_carros()
    limpar_tela()
    menu = '''
    >>> App Carros <<<
    1 - Novo Carro
    2 - Listar Carros
    3 - Listar carros ordenados pelo nome
    4 - Listar carros ordenado pelo ano (desc)
    5 - Buscar por nome
    6 - Listar Carro com Idade

    0 - Sair > '''

    opcao = int(input(menu))

    while opcao != 0:

        if opcao == 1:
            limpar_tela()
            novo_carro = obter_novo_carro()
            carros.append(novo_carro)
            sucesso()
        elif opcao == 2:
            limpar_tela()
            listar_carros(carros)
        elif opcao == 3:
            carros_ordenados = sorted(carros, key=por_nome)
            listar_carros(carros_ordenados)
        elif opcao == 4:
            carros_ordenados = sorted(carros, key=por_ano, reverse=True)
            listar_carros(carros_ordenados)
        elif opcao == 5:
            limpar_tela()
            print('Pesquisa de carros:')
            texto =  input('Nome ou parte: ')
            carros_encontrados = filtrar_por_parte_nome(carros, texto)
            listar_carros(carros_encontrados)
        elif opcao == 6:
            carros_com_idade = map_carros_com_idade(carros)
            for carro in carros_com_idade:
                print('>', carro['nome'], f'{carro["idade"]} anos')
            

        input('Enter to continue...')
        limpar_tela()
        opcao = int(input(menu))


def por_nome(carro):
    return carro['nome']


def por_ano(j):
    return j['ano']


# Funções Principais
def obter_novo_carro():
    print('> Adicionando novo carro')
    nome = input('Nome: ')
    ano = int(input('Ano: '))
    preco = float(input('Preço: '))
    novo_carro = {'nome': nome, 'ano': ano, 'preco': preco}
    
    return novo_carro


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


def map_carros_com_idade(carros):
    nova_lista = []
    ano_corrente = int(input('Digite o ano atual: '))
    for carro in carros:
        novo_carro = {'nome': carro['nome'], 'idade': ano_corrente - carro['ano']}
        nova_lista.append(novo_carro)
    
    return nova_lista


def load_carros():
    arquivo = open('carros.txt')

    linhas = arquivo.readlines()
    carros = []
    for linha in linhas:
        dados = linha.strip().split(',')
        carro = {'nome': dados[0], 'ano': int(dados[1]), 'preco': float(dados[2])}
        carros.append(carro)
    
    arquivo.close()
    return carros

main()