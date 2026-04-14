from utils import obter_int_positivo


def main():
    primeiro_termo = obter_int_positivo('Digite o primeiro termo: ')
    razao = obter_int_positivo('Digite a razao: ')
    num_termos = obter_int_positivo('Digite o número de termos: ')

    
    progressao(primeiro_termo, razao, num_termos)
    soma, media = progressao(primeiro_termo, razao, num_termos)
    print(f'Soma: {soma}, Média {media}')

def progressao(primeiro_termo, razao, num_termos):
    soma = 0
    termo = primeiro_termo
    qtd_termos = 0

    for i in range(primeiro_termo, num_termos + 1):
        print(termo)
        termo += razao
        qtd_termos += 1
        soma += termo

    media = soma / qtd_termos
    return soma, media


if __name__ == "__main__":
    main()