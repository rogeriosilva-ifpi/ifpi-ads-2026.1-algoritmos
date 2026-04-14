def progressao():
    resposta = 'S'
    while resposta == 'S':
        somatorio = 0
        primeiro_termo = int(input('digite o primeiro termo: '))
        razao = int(input('digite a razão da progressão: '))
        n_termos = int(input('digite a quatidade de termos da progressão: '))
        
        while n_termos < 2:
            n_termos = int(input('digite pelo menos dois termos: '))

        print('termos da P.A:', end=' ')

        for i in range(n_termos):
            termo = primeiro_termo + (i * razao)
            somatorio += termo
            print(termo, end=' ')
        
        media = somatorio / n_termos
        print(f'a soma dos termos da P.A é igual a {somatorio}')
        print(f'a média dos termos da P.A é igual a {media}')
        
        resposta = input('voce quer calcular mais uma P.A S/N ? ').upper()
        while resposta != 'S' and resposta != 'N':
            resposta = input('Resposta inválida. Digite S ou N: ').upper()

progressao()

     


