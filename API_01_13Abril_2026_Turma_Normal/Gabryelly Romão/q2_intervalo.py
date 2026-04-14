n = int(input('Digite um numero: '))
m = int(input('Digite outro numero'))

def obter_infe(n):
    for i in range(n):
        if  n % 2 != 0:
            return n
