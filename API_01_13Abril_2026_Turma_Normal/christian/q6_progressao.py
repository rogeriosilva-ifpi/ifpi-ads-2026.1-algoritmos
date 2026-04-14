def main():
    while True:
        termo=int(input('Primeiro termo: '))
        razao=int(input('Razão: '))
        n_termos=int(input('Número de termos: '))
        soma_termos=0
        while n_termos<2:
            n_termos=int(input('Pelo menos 2 termos: '))
        
        for i in range(n_termos):
            termo=termo+razao*i
            print(termo,end=' ')
            soma_termos+=termo
        media_termos=soma_termos/n_termos
        print(f'\nSoma dos termos: {soma_termos}')
        print(f'Média dos termos: {media_termos}')

        continuar = input('Deseja continuar? S/N ')
        if continuar =="S":
            
            

main()