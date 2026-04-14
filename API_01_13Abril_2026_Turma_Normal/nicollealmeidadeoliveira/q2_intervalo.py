from utils import obter_int_positivo


def main():
   while True:
    n = obter_int_positivo('N: ')
    m = obter_int_positivo('M: ')
    if m < n:
       continue

    print('Números: ')
    soma = impar_e_divisivel(n, m)
    print(f'Soma: {soma}')
    break

def impar_e_divisivel(n, m):
    soma = 0

    for i in range(n, m + 1):
        if i % 2 != 0 and i % 3 == 0:
            print(i)
            soma += i
    return soma

if __name__ == "__main__":
    main()