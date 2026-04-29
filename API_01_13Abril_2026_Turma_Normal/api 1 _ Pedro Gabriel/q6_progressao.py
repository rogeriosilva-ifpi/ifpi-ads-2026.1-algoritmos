def main():
    p1 = int(input('Primeiro termo:'))
    razao = int(input('Razão:'))
    n_term = int(input('Numero de termos:'))

    while n_term < 2:
        print('Numero de termos deve ser no minimo 2')
        n_term = int(input('Numero de termos:'))

    pa(p1, razao ,n_term)

def pa(p1, razao ,n_term):
    resultado = p1
    contador = 1
    soma = 0
    print('Termos da sequencia:')
    while contador <= n_term:
        resultado = contador*razao
        print(resultado, end=" ")
        soma = soma+resultado
        contador += 1
    print(f'\nSoma dos termos:{soma}')
    media = soma/n_term
    print(f'Media dos termos:{media}')
    proximo = input('Deseja continuar?(s/n):')
    if proximo == 'n':
        return
    else:
        main()

    

main()