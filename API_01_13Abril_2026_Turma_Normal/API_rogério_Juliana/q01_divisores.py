from utilitaros import inteiro

def main():
    numero = inteiro('insira um numero inteiro: ')
    total = 0
    for i in range(1,numero+1):
        if eh_divisor(numero,i):
            total += 1
    print(f'\ntotal: {total}')
        
    
def eh_divisor(d,i):
    if d % i == 0:
        print(i, end=' ')
        return True
main()