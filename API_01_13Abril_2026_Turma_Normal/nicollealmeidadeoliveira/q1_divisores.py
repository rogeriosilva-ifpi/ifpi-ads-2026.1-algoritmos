from utils import obter_int_positivo

def main():
    n = obter_int_positivo()

    print('Divisores:')
    qtd_divisores = divisores(n)
    print(f'Quantidade de divisores: {qtd_divisores}')


def divisores(n):
    qtd_divisores = 0
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
            qtd_divisores += 1
    return qtd_divisores


if __name__ == "__main__":
    main()