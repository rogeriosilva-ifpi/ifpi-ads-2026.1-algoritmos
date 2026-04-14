def main():
    calcular_progressao()
    continuar_progressao()

def calcular_progressao():
    term_a = int(input('Digite o primeiro termo da progressão: '))
    razao = int(input('Digite a razão da progressão: '))
    num_term = int(input('Digite o número de termos da progressão: '))
    
    while num_term < 2:
        print('Quantidade de termos insuficiente.')
        num_term = int(input('Digite o número de termos da progressão: '))
    prim_term = term_a
    soma = 0
    print('Termos:')
    
    for i in range(prim_term ,num_term, razao):
        print(i)
        soma += i
        prim_term = i
    media = soma / num_term
    print('Soma:', soma)
    print('Media:', media)

def continuar_progressao():
    continuar = input('Deseja continuar?(s/n) ')
    while continuar == 's' or continuar == 's':
        calcular_progressao()

main()